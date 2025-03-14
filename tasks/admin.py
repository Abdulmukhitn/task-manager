# todos/admin.py
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # List display configuration
    list_display = ('title', 'user', 'complete', 'created')
    list_filter = ('complete', 'created', 'user')
    search_fields = ('title', 'description')
    ordering = ('-created',)  # Newest first
    date_hierarchy = 'created'

    # Form customization
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'description')
        }),
        ('Status', {
            'fields': ('complete',),
            'classes': ('collapse',)
        }),
    )

    # Auto-complete for user field
    autocomplete_fields = ['user']


# Optional: Customize User admin if needed
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff')
    search_fields = ('username', 'email')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
