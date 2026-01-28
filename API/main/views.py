from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chat, Message
from django.shortcuts import get_object_or_404

from .serializers import ChatsSerializer, MessageSerializer

# def home(request):
#     return HttpResponse("<h1>Hello, world!</h1><p>This is an HTTP response with HTML tags.</p>")

@api_view(['POST'])
def create_chat(request):
    if request.method == 'POST':

        data = request.data.copy()
        serializer = ChatsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def get_delete_chat(request, id):
    if request.method == 'GET':
        chat = Chat.objects.get(id=id)
        limit_str = request.query_params.get('limit', '20')
        try:
            limit = int(limit_str)
            if limit < 1:
                limit = 20
            elif limit > 100:
                limit = 100
        except ValueError:
            limit = 20

        messages = Message.objects.filter(chat=chat).order_by('created_at')[:limit]
        messages_data = MessageSerializer(messages, many=True).data
        chat_data = ChatsSerializer(chat).data


        response_data = {
            'chat': chat_data,
            'messages': messages_data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        chat = get_object_or_404(Chat, id=id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def send_message(request, id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=id)

        data = request.data.copy()
        data['chat'] = chat.id

        serializer = MessageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
