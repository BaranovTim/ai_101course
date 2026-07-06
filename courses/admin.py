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

admin.site.site_header = "AI 101 Academy — Administration"
admin.site.site_title = "AI 101 Admin"
admin.site.index_title = "Manage courses, learners & payments"


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    show_change_link = True
    fields = ("order", "title", "subtitle", "icon")


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    show_change_link = True
    fields = ("order", "title", "slug", "lesson_type", "duration_minutes")
    prepopulated_fields = {"slug": ("title",)}


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    fields = ("text", "is_correct")


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True
    fields = ("order", "text", "explanation")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "track", "price_display", "student_price_display", "lesson_count", "is_published")
    list_filter = ("track", "is_published")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ModuleInline]
    fieldsets = (
        ("Basics", {"fields": ("title", "slug", "tagline", "description", "is_published")}),
        ("Audience", {
            "fields": ("track",),
            "description": "Learners whose occupation matches the track see this course recommended first.",
        }),
        ("Pricing", {
            "fields": ("price_cents", "student_price_cents"),
            "description": "Prices are in US cents (10000 = $100). The first lesson of every course is always free to preview.",
        }),
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "course", "lesson_total")
    list_filter = ("course",)
    inlines = [LessonInline]

    @admin.display(description="Lessons")
    def lesson_total(self, obj):
        return obj.lessons.count()


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "lesson_type", "duration_minutes", "has_image", "has_quiz")
    list_filter = ("module__course", "module", "lesson_type")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Basics", {"fields": ("module", "order", "title", "slug", "lesson_type", "duration_minutes")}),
        ("Media", {
            "fields": ("image", "video_url"),
            "description": "Optional: an illustration shown at the top of the lesson and/or an embeddable video URL.",
        }),
        ("Content", {
            "fields": ("content", "instructions", "exercise_prompt"),
            "description": (
                "Content is the lesson body (HTML supported: <h2>, <p>, <ul>, <table>, "
                "and the classes 'prompt-box' and 'callout' for styled boxes). "
                "Instructions render in a highlighted step-by-step box. "
                "Exercise prompt renders as a 'Try it yourself' assignment."
            ),
        }),
    )

    @admin.display(boolean=True, description="Image")
    def has_image(self, obj):
        return bool(obj.image)

    @admin.display(boolean=True, description="Quiz")
    def has_quiz(self, obj):
        return Quiz.objects.filter(lesson=obj).exists()


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pass_percent", "question_total")
    list_filter = ("lesson__module__course",)
    inlines = [QuestionInline]

    @admin.display(description="Questions")
    def question_total(self, obj):
        return obj.questions.count()


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "quiz")
    list_filter = ("quiz__lesson__module__course",)
    inlines = [ChoiceInline]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "is_active", "activated_at")
    list_filter = ("is_active", "course")


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
