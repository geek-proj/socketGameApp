from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url
from project.consumers import ChatConsumer,EnterConsumer

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r"^room/",ChatConsumer),
                url(r"^room2/",EnterConsumer)
            ])
        )
    )
})