from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from .models import Task
# from django.http import HttpResponse

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todos/index.html', {'tasks_list':tasks})

def add_task(request):
    return render(request, 'todos/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todos/edit_task.html', {'task': task})

@require_http_methods(['POST'])
def submit_task(request):
    task_title = request.POST['task_title']
    task_description = request.POST['task_description']
    category = request.POST['category']
    created_at = timezone.now()
    task = Task(task_title=task_title, task_description=task_description, category=category, created_at=created_at)
    task.save()
    return redirect('index')

@require_http_methods(['POST'])
def modify_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.task_title = request.POST['task_title']
    task.task_description = request.POST['task_description']
    
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')