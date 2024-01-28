"""
ASGI config for artsWebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# entry point for the asynchronous server | used especially for long-lived connections.

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app.routing import websocket_urlpatterns

# which module to use when Django starts up,
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

application = ProtocolTypeRouter({
    # handles the HTTP request but in an asynchronous way. 
    "http": get_asgi_application(),
    # Then the traffic related to the WebSocket connection
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})



# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artsWebsite.settings')

# application = get_asgi_application()