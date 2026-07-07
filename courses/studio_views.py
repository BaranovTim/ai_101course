"""Studio: in-site course builder for staff — no Django admin required."""
import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Choice, Course, Lesson, Module, Question, Quiz, Track
from .studio_forms import CourseForm, LessonForm, ModuleForm, TrackForm

staff_required = staff_member_required(login_url="login")


@staff_required
def home(request):
    tracks = Track.objects.prefetch_related("courses__modules__lessons")
    orphan_courses = Course.objects.filter(track__isnull=True)
    return render(request, "studio/home.html", {"tracks": tracks, "orphan_courses": orphan_courses})


# ---------- Tracks ----------

@staff_required
def track_create(request):
    form = TrackForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        track = form.save()
        messages.success(request, f"Track “{track.name}” created.")
        return redirect("studio_home")
    return render(request, "studio/track_form.html", {"form": form, "track": None})


@staff_required
def track_edit(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    form = TrackForm(request.POST or None, instance=track)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Track “{track.name}” updated.")
        return redirect("studio_home")
    return render(request, "studio/track_form.html", {"form": form, "track": track})


# ---------- Courses ----------

@staff_required
def course_create(request):
    initial = {}
    track_id = request.GET.get("track")
    if track_id:
        initial["track"] = track_id
    form = CourseForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        course = form.save()
        messages.success(request, f"Course “{course.title}” created — now add modules and lessons.")
        return redirect("studio_course", course_id=course.id)
    return render(request, "studio/course_form.html", {"form": form, "course": None})


@staff_required
def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Course “{course.title}” updated.")
        return redirect("studio_course", course_id=course.id)
    return render(request, "studio/course_form.html", {"form": form, "course": course})


@staff_required
def course_manage(request, course_id):
    course = get_object_or_404(
        Course.objects.select_related("track").prefetch_related("modules__lessons"),
        id=course_id,
    )
    module_form = ModuleForm(initial={"order": course.modules.count() + 1})
    lessons_with_quiz = set(
        Quiz.objects.filter(lesson__module__course=course).values_list("lesson_id", flat=True)
    )
    return render(
        request,
        "studio/course_manage.html",
        {"course": course, "module_form": module_form, "lessons_with_quiz": lessons_with_quiz},
    )


# ---------- Modules ----------

@staff_required
@require_POST
def module_add(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = ModuleForm(request.POST)
    if form.is_valid():
        module = form.save(commit=False)
        module.course = course
        module.save()
        messages.success(request, f"Module “{module.title}” added.")
    else:
        messages.error(request, "Could not add the module — check the fields.")
    return redirect("studio_course", course_id=course.id)


@staff_required
def module_edit(request, module_id):
    module = get_object_or_404(Module.objects.select_related("course"), id=module_id)
    form = ModuleForm(request.POST or None, instance=module)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Module “{module.title}” updated.")
        return redirect("studio_course", course_id=module.course_id)
    return render(request, "studio/module_form.html", {"form": form, "module": module})


@staff_required
@require_POST
def module_delete(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    course_id = module.course_id
    module.delete()
    messages.success(request, "Module deleted (including its lessons).")
    return redirect("studio_course", course_id=course_id)


# ---------- Lessons ----------

@staff_required
def lesson_create(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if not course.modules.exists():
        messages.error(request, "Add a module first — lessons live inside modules.")
        return redirect("studio_course", course_id=course.id)
    initial = {}
    module_id = request.GET.get("module")
    if module_id:
        initial["module"] = module_id
        mod = course.modules.filter(id=module_id).first()
        if mod:
            initial["order"] = mod.lessons.count() + 1
    form = LessonForm(request.POST or None, request.FILES or None, course=course, initial=initial)
    if request.method == "POST" and form.is_valid():
        lesson = form.save()
        messages.success(request, f"Lesson “{lesson.title}” saved.")
        return redirect("studio_course", course_id=course.id)
    return render(request, "studio/lesson_form.html", {"form": form, "course": course, "lesson": None})


@staff_required
def lesson_edit(request, lesson_id):
    lesson = get_object_or_404(Lesson.objects.select_related("module__course"), id=lesson_id)
    course = lesson.module.course
    form = LessonForm(request.POST or None, request.FILES or None, instance=lesson, course=course)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Lesson “{lesson.title}” updated.")
        return redirect("studio_course", course_id=course.id)
    return render(request, "studio/lesson_form.html", {"form": form, "course": course, "lesson": lesson})


@staff_required
@require_POST
def lesson_delete(request, lesson_id):
    lesson = get_object_or_404(Lesson.objects.select_related("module__course"), id=lesson_id)
    course_id = lesson.module.course_id
    lesson.delete()
    messages.success(request, "Lesson deleted.")
    return redirect("studio_course", course_id=course_id)


# ---------- Quiz builder ----------

@staff_required
def quiz_builder(request, lesson_id):
    """One page to edit a lesson's quiz: questions AND answer choices together."""
    lesson = get_object_or_404(Lesson.objects.select_related("module__course"), id=lesson_id)
    quiz = Quiz.objects.filter(lesson=lesson).prefetch_related("questions__choices").first()

    if request.method == "POST":
        try:
            payload = json.loads(request.body or "{}")
            pass_percent = int(payload.get("pass_percent", 70))
            questions = payload.get("questions", [])
        except (ValueError, TypeError):
            return JsonResponse({"error": "Invalid data."}, status=400)

        # Validate before saving anything.
        if not 1 <= pass_percent <= 100:
            return JsonResponse({"error": "Pass mark must be between 1 and 100."}, status=400)
        cleaned = []
        for i, q in enumerate(questions, start=1):
            text = (q.get("text") or "").strip()
            explanation = (q.get("explanation") or "").strip()
            choices = [
                {"text": (c.get("text") or "").strip(), "correct": bool(c.get("correct"))}
                for c in q.get("choices", [])
                if (c.get("text") or "").strip()
            ]
            if not text:
                return JsonResponse({"error": f"Question {i} has no text."}, status=400)
            if len(choices) < 2:
                return JsonResponse({"error": f"Question {i} needs at least 2 answer choices."}, status=400)
            correct_count = sum(1 for c in choices if c["correct"])
            if correct_count != 1:
                return JsonResponse(
                    {"error": f"Question {i} must have exactly one correct choice (has {correct_count})."},
                    status=400,
                )
            cleaned.append({"text": text, "explanation": explanation, "choices": choices})

        with transaction.atomic():
            if not cleaned:
                Quiz.objects.filter(lesson=lesson).delete()
                return JsonResponse({"ok": True, "deleted": True})
            quiz_obj, _ = Quiz.objects.get_or_create(lesson=lesson)
            quiz_obj.pass_percent = pass_percent
            quiz_obj.save()
            quiz_obj.questions.all().delete()
            for order, q in enumerate(cleaned, start=1):
                question = Question.objects.create(
                    quiz=quiz_obj, order=order, text=q["text"], explanation=q["explanation"]
                )
                Choice.objects.bulk_create(
                    [Choice(question=question, text=c["text"], is_correct=c["correct"]) for c in q["choices"]]
                )
        return JsonResponse({"ok": True})

    quiz_json = {"pass_percent": 70, "questions": []}
    if quiz:
        quiz_json = {
            "pass_percent": quiz.pass_percent,
            "questions": [
                {
                    "text": q.text,
                    "explanation": q.explanation,
                    "choices": [{"text": c.text, "correct": c.is_correct} for c in q.choices.all()],
                }
                for q in quiz.questions.all()
            ],
        }
    return render(
        request,
        "studio/quiz_builder.html",
        {"lesson": lesson, "course": lesson.module.course, "quiz_json": quiz_json},
    )
