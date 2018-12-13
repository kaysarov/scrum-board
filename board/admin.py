from __future__ import unicode_literals
from django.contrib import admin  # noqa F401
from .models import Sprint, Task


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('title', 'sprint', 'status', 'priority', 'assigned', 'done')
    list_filter = ('sprint', 'status', 'priority')


@admin.register(Sprint)
class Sprint(admin.ModelAdmin):
    list_display = ('title', 'begin', 'end')
    list_filter = ('end',)
