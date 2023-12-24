from django.urls import path
from . import consumers

wsUrlPatterns = [
    path(r"ws/chat/<str:roomname>/<str:nickname>/", consumers.ChatConsumer.as_asgi())
]