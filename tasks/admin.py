from multiprocessing.resource_tracker import register

from django.contrib import admin
from . models import Profile, Task, Title


admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Title)
