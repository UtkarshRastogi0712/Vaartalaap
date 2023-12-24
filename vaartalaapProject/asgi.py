import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chatApp.routing import wsUrlPatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaartalaapProject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        URLRouter(
           wsUrlPatterns
        )
    )
})

