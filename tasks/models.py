from django.conf import settings
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    IMPORTANCE_CHOICES = [
        ("E", "Easy"),
        ("N", "Normal"),
        ("D", "Difficult"),
    ]


    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )
    importance = models.CharField(
        max_length=1,
        choices=IMPORTANCE_CHOICES,
        default='E'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )



class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Title(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,

    )