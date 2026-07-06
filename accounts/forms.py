from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

INPUT_CLASSES = (
    "w-full rounded-lg border border-outline-variant bg-white px-4 py-3 text-on-surface "
    "placeholder:text-outline focus:border-primary focus:ring-4 focus:ring-primary/10 "
    "focus:outline-none transition"
)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    occupation = forms.ChoiceField(choices=Profile.OCCUPATIONS, required=True, label="Your track")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "first_name": "First name",
            "last_name": "Last name",
            "username": "Choose a username",
            "email": "you@example.ky",
            "password1": "Create a password",
            "password2": "Confirm your password",
        }
        for name, field in self.fields.items():
            field.widget.attrs["class"] = INPUT_CLASSES
            if name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[name]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.profile.occupation = self.cleaned_data["occupation"]
            user.profile.save()
        return user


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60, required=False)
    last_name = forms.CharField(max_length=60, required=False)

    class Meta:
        model = Profile
        fields = ("avatar", "occupation", "district", "learning_goal")
        widgets = {
            "avatar": forms.FileInput(attrs={"accept": "image/*"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "avatar":
                field.widget.attrs["class"] = "block w-full text-sm text-on-surface-variant file:mr-4 file:rounded-lg file:border-0 file:bg-surface-container file:px-4 file:py-2.5 file:text-sm file:font-semibold file:text-primary hover:file:bg-surface-container-high"
            else:
                field.widget.attrs["class"] = INPUT_CLASSES


class StudentIDForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("student_id_document",)
        widgets = {
            "student_id_document": forms.FileInput(attrs={"accept": "image/*"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student_id_document"].required = True
        self.fields["student_id_document"].widget.attrs["class"] = (
            "block w-full text-sm text-on-surface-variant file:mr-4 file:rounded-lg file:border-0 "
            "file:bg-surface-container file:px-4 file:py-2.5 file:text-sm file:font-semibold "
            "file:text-primary hover:file:bg-surface-container-high"
        )
