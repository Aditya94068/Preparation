from django.contrib import admin
from . models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','title','created_date','mark_as_completed')
    list_filter = ('created_date','mark_as_completed')
    search_fields = ('title','name')
    ordering = ('-created_date',)