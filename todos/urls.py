from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add_task, name='add_task'),
    path('create/submit/', views.submit_task, name='submit_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit/update/<int:task_id>/', views.modify_task, name='modify_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
