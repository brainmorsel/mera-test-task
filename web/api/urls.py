from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^heartbeat$', csrf_exempt(views.heartbeat), name='heartbeat'),
    url(r'^uptime$', csrf_exempt(views.uptime), name='uptime'),
]
