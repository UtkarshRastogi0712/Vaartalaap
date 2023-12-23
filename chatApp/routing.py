from django.urls import re_path
from . import consumers

wsUrlPatterns = [
    re_path(r"chat/global/", consumers.ChatConsumer.as_asgi())
]