from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

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

    # Core fields
    title = models.CharField(max_length=100)  # Replaces "Title" model
    description = models.TextField(blank=True)  # Replaces "Description" model
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

    # Relationships
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user = (models.ForeignKey(User, on_delete=models.CASCADE
    ))

    def __str__(self):
        return self.title