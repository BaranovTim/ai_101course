from django.urls import path

from . import studio_views as views

urlpatterns = [
    path("", views.home, name="studio_home"),
    path("tracks/new/", views.track_create, name="studio_track_create"),
    path("tracks/<int:track_id>/", views.track_edit, name="studio_track_edit"),
    path("courses/new/", views.course_create, name="studio_course_create"),
    path("courses/<int:course_id>/", views.course_manage, name="studio_course"),
    path("courses/<int:course_id>/edit/", views.course_edit, name="studio_course_edit"),
    path("courses/<int:course_id>/modules/add/", views.module_add, name="studio_module_add"),
    path("modules/<int:module_id>/edit/", views.module_edit, name="studio_module_edit"),
    path("modules/<int:module_id>/delete/", views.module_delete, name="studio_module_delete"),
    path("courses/<int:course_id>/lessons/new/", views.lesson_create, name="studio_lesson_create"),
    path("lessons/<int:lesson_id>/edit/", views.lesson_edit, name="studio_lesson_edit"),
    path("lessons/<int:lesson_id>/delete/", views.lesson_delete, name="studio_lesson_delete"),
    path("lessons/<int:lesson_id>/quiz/", views.quiz_builder, name="studio_quiz"),
]
