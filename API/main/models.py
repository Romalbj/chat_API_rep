from django.db import models

class Chat(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):

    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Чат: {self.chat}, сообщение: {self.text}'
