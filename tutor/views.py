import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from courses.models import Lesson

from .models import TutorMessage
from .services import get_tutor_reply


@login_required
def tutor_page(request):
    history = TutorMessage.objects.filter(user=request.user)[:100]
    history_json = [{"role": m.role, "content": m.content} for m in history]
    return render(request, "tutor/tutor.html", {"history_json": history_json})


@login_required
@require_POST
def api_chat(request):
    try:
        payload = json.loads(request.body or "{}")
        message = (payload.get("message") or "").strip()
        lesson_id = payload.get("lesson_id")
    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)

    if not message:
        return JsonResponse({"error": "Empty message"}, status=400)
    if len(message) > 4000:
        return JsonResponse({"error": "Message too long"}, status=400)

    lesson = Lesson.objects.filter(id=lesson_id).first() if lesson_id else None

    # Last 12 messages as conversation context
    history = list(TutorMessage.objects.filter(user=request.user).order_by("-created_at")[:12])
    history.reverse()

    TutorMessage.objects.create(user=request.user, role="user", content=message, lesson=lesson)
    reply = get_tutor_reply(request.user, message, history, lesson=lesson)
    TutorMessage.objects.create(user=request.user, role="assistant", content=reply, lesson=lesson)

    return JsonResponse({"reply": reply})
