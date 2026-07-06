from django.contrib import admin

from .models import (
    Certificate,
    Choice,
    Course,
    Enrollment,
    Lesson,
    LessonProgress,
    Module,
    Question,
    Quiz,
    QuizAttempt,
)


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "lesson_type", "duration_minutes")


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "price_display", "is_published")
    inlines = [ModuleInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "course")
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "lesson_type", "duration_minutes")
    list_filter = ("module", "lesson_type")


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pass_percent")
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "quiz")
    inlines = [ChoiceInline]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "is_active", "activated_at")
    list_filter = ("is_active",)


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "completed", "completed_at")
    list_filter = ("completed",)


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "total", "passed", "created_at")
    list_filter = ("passed",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "uid", "issued_at")
