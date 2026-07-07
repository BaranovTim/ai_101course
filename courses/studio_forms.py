from django import forms

from .models import Course, Lesson, Module, Track

INPUT = (
    "w-full rounded-lg border border-outline-variant bg-white px-4 py-3 text-on-surface "
    "placeholder:text-outline focus:border-primary focus:ring-4 focus:ring-primary/10 "
    "focus:outline-none transition"
)
FILE_INPUT = (
    "block w-full text-sm text-on-surface-variant file:mr-4 file:rounded-lg file:border-0 "
    "file:bg-surface-container file:px-4 file:py-2.5 file:text-sm file:font-semibold "
    "file:text-primary hover:file:bg-surface-container-high"
)


def style_fields(form):
    for name, field in form.fields.items():
        if isinstance(field.widget, (forms.ClearableFileInput, forms.FileInput)):
            field.widget.attrs["class"] = FILE_INPUT
        elif isinstance(field.widget, forms.CheckboxInput):
            field.widget.attrs["class"] = "h-5 w-5 rounded border-outline-variant text-primary focus:ring-primary/30"
        else:
            field.widget.attrs["class"] = INPUT


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ("name", "slug", "description", "icon", "audience",
                  "price_cents", "student_price_cents", "order", "is_published")
        widgets = {"description": forms.Textarea(attrs={"rows": 2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        self.fields["slug"].help_text = "Used in the URL, e.g. 'general' or 'accounting'."
        self.fields["price_cents"].help_text = "In US cents: 10000 = $100."
        self.fields["student_price_cents"].help_text = "Optional. In US cents: 5000 = $50."
        self.fields["icon"].help_text = "Material Symbols icon name, e.g. school, calculate, beach_access."


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "slug", "tagline", "description", "track", "is_published")
        widgets = {
            "tagline": forms.Textarea(attrs={"rows": 2}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        self.fields["track"].queryset = Track.objects.all()
        self.fields["track"].help_text = "Buying this track unlocks the course."
        self.fields["slug"].help_text = "Used in the URL, e.g. 'ai-101'."


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ("order", "title", "subtitle", "icon")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("module", "order", "title", "slug", "lesson_type", "duration_minutes",
                  "image", "video_url", "content", "instructions", "exercise_prompt")
        widgets = {
            "content": forms.Textarea(attrs={"rows": 16, "class": "font-mono text-sm"}),
            "instructions": forms.Textarea(attrs={"rows": 5}),
            "exercise_prompt": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, course=None, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        if course is not None:
            self.fields["module"].queryset = course.modules.all()
        self.fields["content"].widget.attrs["class"] += " " + INPUT
        self.fields["content"].help_text = (
            "HTML supported: <h2>, <p>, <ul>, <ol>, <table>. "
            "Use <div class=\"prompt-box\">…</div> for prompt examples and "
            "<div class=\"callout\">…</div> for highlighted notes."
        )
        self.fields["instructions"].help_text = "Optional — shows as a highlighted 'Instructions' box."
        self.fields["exercise_prompt"].help_text = "Optional — shows as a 'Try it yourself' assignment."
        self.fields["image"].help_text = "Optional illustration shown at the top of the lesson."
