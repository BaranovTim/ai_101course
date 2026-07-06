"""Seed the AI 101 course: modules, lessons, quizzes, questions, choices.

Usage: python manage.py seed_course
Idempotent — re-running replaces the course content (user progress on
matching lesson slugs is preserved where possible).
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from courses.course_content_part1 import MODULES_PART1
from courses.course_content_part2 import MODULES_PART2
from courses.models import Choice, Course, Lesson, Module, Question, Quiz

COURSE_SLUG = "ai-101"


class Command(BaseCommand):
    help = "Seed the AI 101 course content (modules, lessons, quizzes)."

    @transaction.atomic
    def handle(self, *args, **options):
        course, created = Course.objects.update_or_create(
            slug=COURSE_SLUG,
            defaults={
                "title": "AI 101: Fundamentals & Practical Applications",
                "tagline": "Master ChatGPT, Claude, and modern AI tools through practical, interactive lessons — no technical background required.",
                "description": (
                    "A beginner-friendly AI course for the Cayman Islands community. "
                    "Learn how AI works, how to write effective prompts, and how to apply "
                    "AI in hospitality, banking, accounting, marketing, and more."
                ),
                "price_cents": 10000,
                "is_published": True,
            },
        )
        self.stdout.write(("Created" if created else "Updated") + f" course: {course.title}")

        modules_data = MODULES_PART1 + MODULES_PART2
        seen_module_ids = []

        for m_order, m in enumerate(modules_data, start=1):
            module, _ = Module.objects.update_or_create(
                course=course,
                order=m_order,
                defaults={"title": m["title"], "subtitle": m["subtitle"], "icon": m["icon"]},
            )
            seen_module_ids.append(module.id)
            seen_lesson_ids = []

            for l_order, l in enumerate(m["lessons"], start=1):
                lesson, _ = Lesson.objects.update_or_create(
                    module=module,
                    slug=l["slug"],
                    defaults={
                        "order": l_order,
                        "title": l["title"],
                        "lesson_type": l["type"],
                        "duration_minutes": l["duration"],
                        "content": l["content"].strip(),
                        "exercise_prompt": (l.get("exercise") or "").strip(),
                        "video_url": l.get("video_url", ""),
                    },
                )
                seen_lesson_ids.append(lesson.id)

                quiz_data = l.get("quiz")
                if quiz_data:
                    quiz, _ = Quiz.objects.update_or_create(
                        lesson=lesson,
                        defaults={
                            "title": "Knowledge check",
                            "pass_percent": quiz_data.get("pass_percent", 70),
                        },
                    )
                    # Rebuild questions each run for a clean, consistent state.
                    quiz.questions.all().delete()
                    for q_order, (q_text, choices, explanation) in enumerate(
                        quiz_data["questions"], start=1
                    ):
                        question = Question.objects.create(
                            quiz=quiz, order=q_order, text=q_text, explanation=explanation
                        )
                        for c_text, is_correct in choices:
                            Choice.objects.create(
                                question=question, text=c_text, is_correct=is_correct
                            )
                else:
                    Quiz.objects.filter(lesson=lesson).delete()

            # Remove lessons no longer in the seed data for this module
            module.lessons.exclude(id__in=seen_lesson_ids).delete()

        course.modules.exclude(id__in=seen_module_ids).delete()

        total_lessons = Lesson.objects.filter(module__course=course).count()
        total_questions = Question.objects.filter(quiz__lesson__module__course=course).count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {course.modules.count()} modules, {total_lessons} lessons, "
                f"{total_questions} quiz questions."
            )
        )
