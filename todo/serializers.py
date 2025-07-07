from rest_framework import serializers
from .models import Task, ContextEntry

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextEntry
        fields = '__all__'
