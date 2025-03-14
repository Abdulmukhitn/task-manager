from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/', views.task_detail, name='detail-task'),
    path('<int:task_id>/form/', views.form_task, name='form-task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete-task'),



]