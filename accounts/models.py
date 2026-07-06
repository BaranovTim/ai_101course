from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    OCCUPATIONS = [
        ("hospitality", "Hospitality & Tourism"),
        ("banking", "Banking & Finance"),
        ("accounting", "Accounting & Audit"),
        ("marketing", "Marketing"),
        ("education", "Education"),
        ("healthcare", "Healthcare"),
        ("construction", "Construction & Real Estate"),
        ("sales", "Sales"),
        ("student", "Student"),
        ("business_owner", "Small Business Owner"),
        ("other", "Other"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    occupation = models.CharField(max_length=30, choices=OCCUPATIONS, default="other")
    district = models.CharField(max_length=100, blank=True, help_text="e.g. George Town, West Bay, Bodden Town")
    learning_goal = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Profile of {self.user}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
