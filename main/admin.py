'''Настройка админ панели'''
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Управление вопросами в админ. панели'''
    list_display = ('text', 'option1', 'option2', 'correct')