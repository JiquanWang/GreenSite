from django.db import models

# Create your models here.


class FlowerShelf(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower_shelf'
