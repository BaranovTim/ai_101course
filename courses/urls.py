from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("courses/", views.courses_list, name="courses"),
    path("pricing/", views.pricing, name="pricing"),
    path("industries/", views.industries, name="industries"),
    path("course/<slug:slug>/", views.course_overview, name="course_overview"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("learn/<slug:course_slug>/", views.my_learning, name="my_learning"),
    path("learn/<slug:course_slug>/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    path("certificates/", views.certificates, name="certificates"),
    path("certificates/<uuid:uid>/download/", views.certificate_download, name="certificate_download"),
    # JSON APIs used by the React components
    path("api/lessons/<int:lesson_id>/complete/", views.api_complete_lesson, name="api_complete_lesson"),
    path("api/lessons/<int:lesson_id>/quiz/", views.api_quiz, name="api_quiz"),
    path("api/lessons/<int:lesson_id>/quiz/submit/", views.api_quiz_submit, name="api_quiz_submit"),
]
