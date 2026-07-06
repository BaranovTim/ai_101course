import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from courses.models import Course, Enrollment

from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


def stripe_configured():
    return bool(settings.STRIPE_SECRET_KEY and settings.STRIPE_PUBLISHABLE_KEY)


def activate_enrollment(user, course):
    enrollment, _ = Enrollment.objects.get_or_create(user=user, course=course)
    if not enrollment.is_active:
        enrollment.is_active = True
        enrollment.activated_at = timezone.now()
        enrollment.save()
    return enrollment


@login_required
@require_POST
def checkout(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug, is_published=True)

    enrollment = Enrollment.objects.filter(user=request.user, course=course, is_active=True).first()
    if enrollment:
        messages.info(request, "You already own this course.")
        return redirect("dashboard")

    if not stripe_configured():
        # Local dev mode: no Stripe keys yet — show a simulated checkout page
        # so the full purchase flow can be exercised end to end.
        payment = Payment.objects.create(
            user=request.user,
            course=course,
            amount_cents=course.price_cents,
            status="pending",
        )
        return render(
            request,
            "payments/simulated_checkout.html",
            {"course": course, "payment": payment},
        )

    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_email=request.user.email or None,
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": course.price_cents,
                    "product_data": {
                        "name": course.title,
                        "description": course.tagline,
                    },
                },
                "quantity": 1,
            }
        ],
        metadata={"user_id": request.user.id, "course_id": course.id},
        success_url=request.build_absolute_uri("/payments/success/") + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri("/payments/cancel/"),
    )
    Payment.objects.create(
        user=request.user,
        course=course,
        stripe_session_id=session.id,
        amount_cents=course.price_cents,
        status="pending",
    )
    return redirect(session.url, permanent=False)


@login_required
@require_POST
def simulate_payment(request, payment_id):
    """Dev-mode only: completes a simulated purchase when Stripe keys are absent."""
    if stripe_configured():
        return redirect("pricing")
    payment = get_object_or_404(Payment, id=payment_id, user=request.user, status="pending")
    payment.status = "simulated"
    payment.save()
    activate_enrollment(request.user, payment.course)
    messages.success(request, "Payment simulated — you're enrolled! Add Stripe keys in .env to take real payments.")
    return redirect("payment_success")


@login_required
def payment_success(request):
    session_id = request.GET.get("session_id")
    if session_id and stripe_configured():
        # Verify with Stripe directly so enrollment works even before
        # the webhook is configured locally.
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            if session.payment_status == "paid":
                payment = Payment.objects.filter(stripe_session_id=session_id).first()
                if payment and payment.status != "paid":
                    payment.status = "paid"
                    payment.stripe_payment_intent = session.payment_intent or ""
                    payment.save()
                    activate_enrollment(payment.user, payment.course)
        except stripe.error.StripeError:
            pass
    course = Course.objects.filter(is_published=True).first()
    return render(request, "payments/success.html", {"course": course})


@login_required
def payment_cancel(request):
    return render(request, "payments/cancel.html")


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    if not settings.STRIPE_WEBHOOK_SECRET:
        return HttpResponse(status=400)
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        payment = Payment.objects.filter(stripe_session_id=session["id"]).first()
        if payment:
            payment.status = "paid"
            payment.stripe_payment_intent = session.get("payment_intent") or ""
            payment.save()
            activate_enrollment(payment.user, payment.course)
    return HttpResponse(status=200)
