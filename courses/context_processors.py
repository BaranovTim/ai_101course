from .models import Course, Enrollment


def sidebar_course(request):
    """Course used by the sidebar 'My Learning' link: the first course of the
    user's first owned track, falling back to the first published course."""
    course = None
    if request.user.is_authenticated:
        enrollment = (
            Enrollment.objects.filter(user=request.user, is_active=True)
            .select_related("track")
            .first()
        )
        if enrollment and enrollment.track:
            course = enrollment.track.published_courses().first()
    if course is None:
        course = Course.objects.filter(is_published=True).first()
    return {"sidebar_course": course}
