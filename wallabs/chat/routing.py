from django.urls import path, include


# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi()),
]
