from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('add/',views.task_add,name='task_add'),
    path('delete/',views.task_delete,name='task_delete'),
    path('edit/',views.task_edit,name='task_edit'),
]

