from django.contrib import admin

from .models import TutorMessage


@admin.register(TutorMessage)
class TutorMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "created_at")
    list_filter = ("role",)
