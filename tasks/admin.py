# INF601 - Advanced Programming in Python
# Adeola Ajayi
# Mini Project 6

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'completed',
        'created_at',
    )

    list_filter = ('completed', 'created_at')

    search_fields = ('title', 'description')
