from django.urls import path

from . import views

urlpatterns = [
    path("checkout/<slug:course_slug>/", views.checkout, name="checkout"),
    path("simulate/<int:payment_id>/", views.simulate_payment, name="simulate_payment"),
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
]
