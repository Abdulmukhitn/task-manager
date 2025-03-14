from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'  # Replace with your actual app name

    def ready(self):
        # This method is called when the app is ready
        # You can put any initialization code here
        # For example, importing signal handlers
        # import tasks.signals
        pass