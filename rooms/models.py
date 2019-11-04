from django.db import models

# Create your models here.


class RoomInfo(models.Model):
    room_num = models.CharField(max_length=16, blank=True, null=True)
    room_name = models.CharField(max_length=16, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_info'

    def __str__(self):
        return self.room_name
