import uuid

from django.conf import settings
from django.db import models


class Course(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    price_cents = models.PositiveIntegerField(default=10000)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def price_display(self):
        return f"${self.price_cents / 100:,.0f}"

    def lesson_count(self):
        return Lesson.objects.filter(module__course=self).count()


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, default="school", help_text="Material Symbols icon name")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Module {self.order}: {self.title}"


class Lesson(models.Model):
    TYPE_CHOICES = [
        ("reading", "Reading"),
        ("video", "Video"),
        ("exercise", "Interactive Lab"),
    ]
    module = models.ForeignKey(Module, related_name="lessons", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=220)
    title = models.CharField(max_length=220)
    lesson_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="reading")
    duration_minutes = models.PositiveIntegerField(default=10)
    video_url = models.URLField(blank=True)
    content = models.TextField(blank=True, help_text="Lesson body as HTML")
    exercise_prompt = models.TextField(blank=True, help_text="Practical assignment shown at the end of the lesson")

    class Meta:
        ordering = ["module__order", "order"]
        unique_together = [("module", "slug")]

    def __str__(self):
        return self.title


class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, related_name="quiz", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Knowledge check")
    pass_percent = models.PositiveIntegerField(default=70)

    class Meta:
        verbose_name_plural = "quizzes"

    def __str__(self):
        return f"Quiz: {self.lesson.title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    text = models.TextField()
    explanation = models.TextField(blank=True, help_text="Shown after answering to explain the correct choice")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text[:80]


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:80]


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    activated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "course")]

    def __str__(self):
        return f"{self.user} → {self.course}"


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="lesson_progress", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name="progress", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = [("user", "lesson")]
        verbose_name_plural = "lesson progress"


class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="quiz_attempts", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="attempts", on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    passed = models.BooleanField(default=False)
    answers = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def percent(self):
        return round(self.score / self.total * 100) if self.total else 0


class Certificate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="certificates", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="certificates", on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    issued_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "course")]

    def __str__(self):
        return f"Certificate {self.uid}"
