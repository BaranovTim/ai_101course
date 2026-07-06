from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ProfileForm, SignUpForm, StudentIDForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Welcome to AI 101 Academy! The first lesson of every course is free — pick one to try.",
            )
            return redirect("courses")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def settings_view(request):
    profile = request.user.profile
    profile_form = ProfileForm(
        instance=profile,
        initial={"first_name": request.user.first_name, "last_name": request.user.last_name},
    )
    student_form = StudentIDForm(instance=profile)

    if request.method == "POST":
        if "save_profile" in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                request.user.first_name = profile_form.cleaned_data.get("first_name") or request.user.first_name
                request.user.last_name = profile_form.cleaned_data.get("last_name") or request.user.last_name
                request.user.save()
                messages.success(request, "Profile updated.")
                return redirect("settings")
        elif "submit_student_id" in request.POST:
            student_form = StudentIDForm(request.POST, request.FILES, instance=profile)
            if student_form.is_valid():
                p = student_form.save(commit=False)
                if p.student_status != "approved":
                    p.student_status = "pending"
                p.save()
                messages.success(
                    request,
                    "Student ID submitted — we'll review it shortly. Once approved, the student price applies automatically at checkout.",
                )
                return redirect("settings")

    return render(
        request,
        "accounts/settings.html",
        {"form": profile_form, "student_form": student_form, "profile": profile},
    )


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("settings")
    success_message = "Your password has been changed."
