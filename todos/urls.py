from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:id>', views.task_detail, name='task_detail'),

    # path('', views.index, name='index'),
    # path('create/', views.add_task, name='add_task'),
    # path('create/submit/', views.submit_task, name='submit_task'),
    # path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('edit/update/<int:task_id>/', views.modify_task, name='modify_task'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

urlpatterns = format_suffix_patterns(urlpatterns)