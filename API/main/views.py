from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chat, Message
from django.shortcuts import get_object_or_404
from .serializers import ChatsSerializer, MessageSerializer
from .utils import getChatById, get_chat, delete_chat



@api_view(['POST'])
def create_chat(request):
    serializer = ChatsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def get_delete_chat(request, id):
    if request.method == 'GET':
        return get_chat(request, id)
    elif request.method == 'DELETE':
        return delete_chat(request, id)


@api_view(['POST'])
def send_message(request, id):
    chat, error = getChatById(id)
    if error is not None:
        return error

    data = request.data.copy()
    data['chat'] = chat.id
    serializer = MessageSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(error, status=status.HTTP_400_BAD_REQUEST)
