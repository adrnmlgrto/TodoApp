from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 
                  'task_title', 
                  'task_description', 
                  'category', 
                  'is_done', 
                  'created_at']
