from rest_framework import status
from rest_framework.response import Response
from .models import Chat, Message
from .serializers import MessageSerializer, ChatsSerializer


def getChatById(id):
    try:
        return Chat.objects.get(id=id), None
    except Chat.DoesNotExist:
        error_response = Response(
            {'error': 'Чат с таким ID не найден'},
            status=status.HTTP_404_NOT_FOUND
        )
        return None, error_response





def get_chat(request, id):
    chat, error = getChatById(id)
    if error is not None:
        return error

    if request.method == 'GET':
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

def delete_chat(request, id):
    chat, error = getChatById(id)
    if error is not None:
        return error

    try:
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Chat.DoesNotExist:
        return error

