from django.contrib import admin
from django.utils.html import format_html

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "occupation", "district", "student_status", "id_preview")
    list_filter = ("occupation", "student_status")
    search_fields = ("user__username", "user__email")
    actions = ["approve_student", "reject_student"]
    readonly_fields = ("id_preview",)
    fields = ("user", "occupation", "district", "learning_goal", "avatar",
              "student_id_document", "id_preview", "student_status")

    @admin.display(description="Student ID")
    def id_preview(self, obj):
        if obj.student_id_document:
            return format_html(
                '<a href="{0}" target="_blank"><img src="{0}" style="max-height:120px;border-radius:8px"/></a>',
                obj.student_id_document.url,
            )
        return "—"

    @admin.action(description="Approve student verification (activates student pricing)")
    def approve_student(self, request, queryset):
        updated = queryset.update(student_status="approved")
        self.message_user(request, f"{updated} profile(s) approved for student pricing.")

    @admin.action(description="Reject student verification")
    def reject_student(self, request, queryset):
        updated = queryset.update(student_status="rejected")
        self.message_user(request, f"{updated} profile(s) rejected.")
