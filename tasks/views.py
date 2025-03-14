from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            return redirect('task-list')
        else:
            form = TaskForm()


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_details.html')

def form_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # instance=task обновляет существующую задачу
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)  # Форма с текущими данными задачи
    return render(request, 'task_forms.html', {'form': form})

from django.shortcuts import get_object_or_404

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получить задачу или показать 404
    if request.method == 'POST':
        task.delete()  # Удалить задачу
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})


