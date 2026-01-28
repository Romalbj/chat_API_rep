from . import views
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('chats/', views.create_chat, name='create_chat'),
    path('chats/<id>', views.get_delete_chat, name='get_chat'),
    path('chats/<id>/messages', views.send_message, name='send_message'),
]