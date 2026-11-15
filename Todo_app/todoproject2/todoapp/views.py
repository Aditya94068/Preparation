from django.shortcuts import render,redirect
from django.urls import reverse
from . models import Task

def task_list(request):
    task = Task.objects.all().order_by('-created_date')
    return render(request,'task_list.html', {'tasks':task})
def task_add(request):
    pass

def task_delete(request):
    pass

def task_edit(request):
    pass
