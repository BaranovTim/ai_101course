import json

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from .certificates import build_certificate_pdf
from .models import (
    Certificate,
    Course,
    Enrollment,
    Lesson,
    LessonProgress,
    Quiz,
    QuizAttempt,
)


def get_course():
    return Course.objects.filter(is_published=True).first()


def get_enrollment(user, course):
    if not user.is_authenticated or course is None:
        return None
    return Enrollment.objects.filter(user=user, course=course).first()


def course_progress(user, course):
    """Return (completed_count, total_count, percent, completed_ids)."""
    total = Lesson.objects.filter(module__course=course).count()
    completed_ids = set(
        LessonProgress.objects.filter(
            user=user, lesson__module__course=course, completed=True
        ).values_list("lesson_id", flat=True)
    )
    done = len(completed_ids)
    percent = round(done / total * 100) if total else 0
    return done, total, percent, completed_ids


def next_lesson_for(user, course, completed_ids):
    for lesson in Lesson.objects.filter(module__course=course).order_by("module__order", "order"):
        if lesson.id not in completed_ids:
            return lesson
    return None


def maybe_issue_certificate(user, course):
    done, total, percent, _ = course_progress(user, course)
    if total and done == total:
        cert, _ = Certificate.objects.get_or_create(user=user, course=course)
        return cert
    return None


# ---------- Public pages ----------

def landing(request):
    course = get_course()
    enrollment = get_enrollment(request.user, course)
    return render(request, "courses/landing.html", {"course": course, "enrollment": enrollment})


def pricing(request):
    course = get_course()
    enrollment = get_enrollment(request.user, course)
    return render(request, "courses/pricing.html", {"course": course, "enrollment": enrollment})


def industries(request):
    course = get_course()
    return render(request, "courses/industries.html", {"course": course})


def course_overview(request, slug):
    course = get_object_or_404(
        Course.objects.prefetch_related(
            Prefetch("modules__lessons", queryset=Lesson.objects.order_by("order"))
        ),
        slug=slug,
        is_published=True,
    )
    enrollment = get_enrollment(request.user, course)
    completed_ids = set()
    if request.user.is_authenticated:
        _, _, _, completed_ids = course_progress(request.user, course)
    return render(
        request,
        "courses/course_overview.html",
        {"course": course, "enrollment": enrollment, "completed_ids": completed_ids},
    )


# ---------- Learner pages ----------

@login_required
def dashboard(request):
    course = get_course()
    if course is None:
        raise Http404("No course published yet.")
    enrollment = get_enrollment(request.user, course)
    done, total, percent, completed_ids = course_progress(request.user, course)
    nxt = next_lesson_for(request.user, course, completed_ids)
    certificate = Certificate.objects.filter(user=request.user, course=course).first()
    attempts = QuizAttempt.objects.filter(user=request.user).select_related("quiz__lesson")[:5]

    modules = []
    for module in course.modules.prefetch_related("lessons"):
        lessons = list(module.lessons.all())
        m_done = sum(1 for l in lessons if l.id in completed_ids)
        modules.append(
            {
                "module": module,
                "done": m_done,
                "total": len(lessons),
                "percent": round(m_done / len(lessons) * 100) if lessons else 0,
            }
        )

    return render(
        request,
        "courses/dashboard.html",
        {
            "course": course,
            "enrollment": enrollment,
            "done": done,
            "total": total,
            "percent": percent,
            "next_lesson": nxt,
            "certificate": certificate,
            "attempts": attempts,
            "module_stats": modules,
        },
    )


@login_required
def my_learning(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    enrollment = get_enrollment(request.user, course)
    if enrollment is None or not enrollment.is_active:
        return redirect("pricing")
    done, total, percent, completed_ids = course_progress(request.user, course)
    nxt = next_lesson_for(request.user, course, completed_ids)
    return render(
        request,
        "courses/my_learning.html",
        {
            "course": course,
            "enrollment": enrollment,
            "done": done,
            "total": total,
            "percent": percent,
            "completed_ids": completed_ids,
            "next_lesson": nxt,
        },
    )


@login_required
def lesson_detail(request, course_slug, lesson_id):
    course = get_object_or_404(Course, slug=course_slug)
    enrollment = get_enrollment(request.user, course)
    if enrollment is None or not enrollment.is_active:
        return redirect("pricing")
    lesson = get_object_or_404(Lesson, id=lesson_id, module__course=course)

    ordered = list(Lesson.objects.filter(module__course=course).order_by("module__order", "order"))
    idx = ordered.index(lesson)
    prev_lesson = ordered[idx - 1] if idx > 0 else None
    next_lesson = ordered[idx + 1] if idx < len(ordered) - 1 else None

    done, total, percent, completed_ids = course_progress(request.user, course)
    has_quiz = Quiz.objects.filter(lesson=lesson).exists()

    return render(
        request,
        "courses/lesson_detail.html",
        {
            "course": course,
            "lesson": lesson,
            "module": lesson.module,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
            "lesson_number": idx + 1,
            "lesson_total": len(ordered),
            "percent": percent,
            "completed": lesson.id in completed_ids,
            "completed_ids": completed_ids,
            "has_quiz": has_quiz,
        },
    )


@login_required
def certificates(request):
    certs = Certificate.objects.filter(user=request.user).select_related("course")
    course = get_course()
    done, total, percent, _ = course_progress(request.user, course) if course else (0, 0, 0, set())
    return render(
        request,
        "courses/certificates.html",
        {"certs": certs, "course": course, "percent": percent, "done": done, "total": total},
    )


@login_required
def certificate_download(request, uid):
    cert = get_object_or_404(Certificate, uid=uid, user=request.user)
    buf = build_certificate_pdf(cert)
    return FileResponse(buf, as_attachment=True, filename=f"AI101-Certificate-{cert.uid}.pdf")


# ---------- JSON APIs ----------

def _active_lesson_or_none(user, lesson_id):
    lesson = Lesson.objects.filter(id=lesson_id).select_related("module__course").first()
    if lesson is None:
        return None
    enrollment = Enrollment.objects.filter(
        user=user, course=lesson.module.course, is_active=True
    ).first()
    return lesson if enrollment else None


@login_required
@require_POST
def api_complete_lesson(request, lesson_id):
    lesson = _active_lesson_or_none(request.user, lesson_id)
    if lesson is None:
        return JsonResponse({"error": "Not enrolled"}, status=403)
    progress, _ = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    if not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()
    cert = maybe_issue_certificate(request.user, lesson.module.course)
    done, total, percent, _ = course_progress(request.user, lesson.module.course)
    return JsonResponse(
        {
            "completed": True,
            "done": done,
            "total": total,
            "percent": percent,
            "certificate_issued": bool(cert),
        }
    )


@login_required
@require_GET
def api_quiz(request, lesson_id):
    lesson = _active_lesson_or_none(request.user, lesson_id)
    if lesson is None:
        return JsonResponse({"error": "Not enrolled"}, status=403)
    quiz = Quiz.objects.filter(lesson=lesson).prefetch_related("questions__choices").first()
    if quiz is None:
        return JsonResponse({"error": "No quiz for this lesson"}, status=404)
    data = {
        "quiz_id": quiz.id,
        "title": quiz.title,
        "pass_percent": quiz.pass_percent,
        "questions": [
            {
                "id": q.id,
                "text": q.text,
                "choices": [{"id": c.id, "text": c.text} for c in q.choices.all()],
            }
            for q in quiz.questions.all()
        ],
    }
    return JsonResponse(data)


@login_required
@require_POST
def api_quiz_submit(request, lesson_id):
    lesson = _active_lesson_or_none(request.user, lesson_id)
    if lesson is None:
        return JsonResponse({"error": "Not enrolled"}, status=403)
    quiz = Quiz.objects.filter(lesson=lesson).prefetch_related("questions__choices").first()
    if quiz is None:
        return JsonResponse({"error": "No quiz for this lesson"}, status=404)

    try:
        payload = json.loads(request.body or "{}")
        answers = {int(k): int(v) for k, v in payload.get("answers", {}).items()}
    except (ValueError, TypeError, AttributeError):
        return JsonResponse({"error": "Invalid payload"}, status=400)

    questions = list(quiz.questions.all())
    results = []
    score = 0
    for q in questions:
        correct_choice = next((c for c in q.choices.all() if c.is_correct), None)
        picked_id = answers.get(q.id)
        is_right = correct_choice is not None and picked_id == correct_choice.id
        if is_right:
            score += 1
        results.append(
            {
                "question_id": q.id,
                "correct_choice_id": correct_choice.id if correct_choice else None,
                "picked_choice_id": picked_id,
                "is_correct": is_right,
                "explanation": q.explanation,
            }
        )

    total = len(questions)
    percent = round(score / total * 100) if total else 0
    passed = percent >= quiz.pass_percent

    QuizAttempt.objects.create(
        user=request.user,
        quiz=quiz,
        score=score,
        total=total,
        passed=passed,
        answers={str(k): v for k, v in answers.items()},
    )

    certificate_issued = False
    if passed:
        progress, _ = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save()
        certificate_issued = bool(maybe_issue_certificate(request.user, lesson.module.course))

    return JsonResponse(
        {
            "score": score,
            "total": total,
            "percent": percent,
            "passed": passed,
            "pass_percent": quiz.pass_percent,
            "results": results,
            "certificate_issued": certificate_issued,
        }
    )
