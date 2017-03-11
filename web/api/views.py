import json

from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotAllowed

from .models import ServerHeartbeat
from .decorators import basicauth


def heartbeat(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    if request.content_type != 'application/json':
        return HttpResponseBadRequest()

    json_str = request.body.decode('utf-8')
    json_obj = json.loads(json_str)

    if not json_obj.get('server_fqdn'):
        return HttpResponseBadRequest()

    sh = ServerHeartbeat()
    sh.server_fqdn = json_obj['server_fqdn']
    sh.save()

    return JsonResponse({'success': True})


@basicauth
def uptime(request):
    return JsonResponse(ServerHeartbeat.uptime(), safe=False)
