from django.conf import settings
from django.db import models


class TutorMessage(models.Model):
    ROLE_CHOICES = [("user", "User"), ("assistant", "Assistant")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tutor_messages", on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    lesson = models.ForeignKey("courses.Lesson", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.role}: {self.content[:60]}"
