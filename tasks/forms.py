from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        exclude = ('created_at', 'updated_at')

