from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.cache import cache

from todo.models import Task

from .serializers import TaskSerializer

class Ready(APIView):

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'msg': 'Ready'
            },
            status = status.HTTP_200_OK
        )

class Todo(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        tasks = Task.objects.filter(user_id = user_id)
        serial = TaskSerializer(tasks, many = True)
        return Response(data = serial.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CacheTest(APIView):

    def get(self, request, *args, **kwargs):
        key = request.query_params.get('key')
        value = cache.get(key)
    
        return Response({
            key: value
    }, status = status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        key = request.data.get('key')
        value = request.data.get('value')
        cache.set(key=key, value=value)
        return Response({
            key: cache.get(key)
        }, status = 201)