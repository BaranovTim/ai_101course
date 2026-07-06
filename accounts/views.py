from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to AI 101 Academy! Your account is ready.")
            return redirect("pricing")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def settings_view(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data.get("first_name") or request.user.first_name
            request.user.last_name = form.cleaned_data.get("last_name") or request.user.last_name
            request.user.save()
            messages.success(request, "Profile updated.")
            return redirect("settings")
    else:
        form = ProfileForm(
            instance=profile,
            initial={"first_name": request.user.first_name, "last_name": request.user.last_name},
        )
    return render(request, "accounts/settings.html", {"form": form})
