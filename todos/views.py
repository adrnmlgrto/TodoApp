from django.http import JsonResponse
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def task_list(request, format=None):
    # Get all Tasks | Serialize | Return JSON
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])    
def task_detail(request, id, format=None):

    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_http_methods
# from django.utils import timezone
# from .models import Task
# # from django.http import HttpResponse

# def index(request):
#     tasks = Task.objects.all()
#     return render(request, 'todos/index.html', {'tasks_list':tasks})

# def add_task(request):
#     return render(request, 'todos/add_task.html')

# def edit_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     return render(request, 'todos/edit_task.html', {'task': task})

# @require_http_methods(['POST'])
# def submit_task(request):
#     # View for handling user adding new task to list
#     task_title = request.POST['task_title']
#     task_description = request.POST['task_description']
#     category = request.POST['category']
#     task = Task(task_title=task_title, task_description=task_description, category=category)
#     task.save()
#     return redirect('index')

# @require_http_methods(['POST'])
# def modify_task(request, task_id):
#     # View for updating task in /editz
#     task = Task.objects.get(id=task_id)
#     task.task_title = request.POST['task_title']
#     task.task_description = request.POST['task_description']
#     task.category = request.POST['category']
#     task.is_done = bool(request.POST['is_done'])
    
#     task.save()
#     return redirect('index')


# def delete_task(request, task_id):
#     task = Task.objects.get(id=task_id)
#     task.delete()
#     return redirect('index')