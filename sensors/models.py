from django.db import models

# Create your models here.


class SensorInfo(models.Model):
    sensor_num = models.CharField(max_length=32, blank=True, null=True)
    device_mac = models.CharField(max_length=32, blank=True, null=True)
    device_index = models.IntegerField(blank=True, null=True)
    sensor_type_id = models.IntegerField(blank=True, null=True)
    belongto_type = models.IntegerField(blank=True, null=True)
    belongto_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_info'


class SensorType(models.Model):
    sensor_type = models.CharField(max_length=16, blank=True, null=True)
    sensor_type_unit = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_type'

