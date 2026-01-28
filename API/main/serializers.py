from rest_framework import serializers
from .models import Chat, Message

class ChatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        field = '__al__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        field = '__al__'
