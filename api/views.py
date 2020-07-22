from django.shortcuts import render
from .models import Task

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks=Task.objects.filter(user=request.user,completed=False)
    serializer=TaskSerializer(tasks,many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    user=request.user
    if task.user !=user:
        return Response({'response':'you are not permission to delete'})
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    
    user=request.user
    if task.user !=user:
        return Response({'response':'you are not permission to delete'})

    task.delete()

    return Response({'response':'Delete Done!'})