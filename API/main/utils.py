from rest_framework import status
from rest_framework.response import Response
from .models import Chat
def get_chat(id):
    try:
        return Chat.objects.get(id=id), None
    except Chat.DoesNotExist:
        error_response = Response(
            {'error': 'Чат с таким ID не найден'},
            status=status.HTTP_404_NOT_FOUND
        )
        return None, error_response