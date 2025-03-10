from django.db import models

class TaskManager(models.Model):
    task_name = models.CharField(max_length=100)
