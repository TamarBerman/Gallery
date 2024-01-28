from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # as_asgi() create an instance of the consumer in an ASGI-compatible format
        re_path(r'ws/chat/(?P<username>\w+)/$', ChatConsumer.as_asgi()),
    ]