from django.urls import path

from . import views

urlpatterns = [
    path("", views.tutor_page, name="tutor"),
    path("api/chat/", views.api_chat, name="tutor_chat"),
]
