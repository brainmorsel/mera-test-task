from datetime import timedelta

from django.db import models
from django.utils.timezone import now


class ServerHeartbeat(models.Model):
    server_fqdn = models.CharField(db_index=True, max_length=255)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)

    @classmethod
    def uptime(cls):
        period = 24
        time_threshold = now() - timedelta(hours=period)
        result = cls.objects \
            .filter(timestamp__gt=time_threshold) \
            .values('server_fqdn') \
            .annotate(uptime=models.ExpressionWrapper(
                models.Count('server_fqdn'),
                output_field=models.FloatField()
            ) / (60.0 * period))

        return [i for i in result]
