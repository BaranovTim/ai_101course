from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "amount_cents", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("user__username", "stripe_session_id")
