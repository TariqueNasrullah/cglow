from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/judge/(?P<contest_name>[^/]+)/$', consumers.JudgeConsumer),
]