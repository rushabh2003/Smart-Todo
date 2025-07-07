from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, ContextEntry
from .serializers import TaskSerializer, ContextSerializer
from .ai import get_task_ai_suggestions

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ContextViewSet(viewsets.ModelViewSet):
    queryset = ContextEntry.objects.all()
    serializer_class = ContextSerializer

@api_view(['POST'])
def ai_suggestion_view(request):
    title = request.data.get('title')
    context_data = request.data.get('context', [])
    ai_response = get_task_ai_suggestions(title, context_data)
    return Response(ai_response)
