from django.db import models
from rooms.models import RoomInfo
from sensors.models import SensorInfo
from relays.models import RelayInfo
import datetime
# Create your models here.


class FlowerShelf(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower_shelf'

    def __str__(self):
        return self.name

    def belongto_room(self):
        return RoomInfo.objects.get(id=self.room_id)

    def created_datatime(self):
        return datetime.datetime.fromtimestamp(self.created_time).strftime("%Y-%m-%d %H:%M:%S")

    def sensors_count(self):
        return SensorInfo.objects.filter(belongto_type=1, belongto_id=self.id).count()

    def relays_count(self):
        return RelayInfo.objects.filter(belongto_type=1, belongto_id=self.id).count()
