from django.db import models

# Create your models here.


class RelayInfo(models.Model):
    relay_num = models.CharField(max_length=32, blank=True, null=True)
    relay_name = models.CharField(max_length=32, blank=True, null=True)
    device_mac = models.CharField(max_length=32, blank=True, null=True)
    belongto_type = models.IntegerField(blank=True, null=True)
    belongto_id = models.IntegerField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    refresh_time = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    relay_type_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relay_info'
