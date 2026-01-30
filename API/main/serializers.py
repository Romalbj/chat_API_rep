from rest_framework import serializers
from .models import Chat, Message

class ChatsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        trim_whitespace=True,
        required=False,
        error_messages={
            'blank': 'Название чата должно содержать хотя бы 1 символ (не пробел)',
        }
    )

    class Meta:
        model = Chat
        # fields = '__all__'
        fields = ['id', 'title', 'created_at']
        read_only_fields = ['id', 'created_at']


    def validate_title(self, title):
        if len(title) == 0:
            raise serializers.ValidationError('Название чата должно содержать хотя бы 1 символ (не пробел)')
        elif len(title) > 200:
            raise serializers.ValidationError('Название чата не может превышать 200 символов.')
        return title


class MessageSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        trim_whitespace=True,
        required=False,
        error_messages={
            'blank': 'Текст должен состоять хотя бы 1 символ (не пробел)',
        }
    )

    class Meta:
        model = Message
        # fields = '__all__'

        fields = ['id', 'text', 'created_at', 'chat']
        read_only_fields = ['id', 'created_at']

    def validate_text(self, text):
        if len(text) == 0:
            raise serializers.ValidationError('Текст должен состоять хотя бы 1 символ (не пробел)')
        elif len(text) > 5000:
            raise serializers.ValidationError('Длина текста не может превышать 5 000 символов.')
        return text
