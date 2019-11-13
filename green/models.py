# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class ControlData(models.Model):
    relay_num = models.CharField(max_length=32, blank=True, null=True)
    relay_name = models.CharField(max_length=32, blank=True, null=True)
    belongto_type = models.IntegerField(blank=True, null=True)
    belongto_id = models.IntegerField(blank=True, null=True)
    relay_type = models.IntegerField(blank=True, null=True)
    relay_value = models.FloatField(blank=True, null=True)
    collect_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_data'


class DataRecord(models.Model):
    sensor_num = models.CharField(max_length=32, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    object_type = models.IntegerField(blank=True, null=True)
    sensor_type_id = models.CharField(max_length=11, blank=True, null=True)
    sensor_value = models.FloatField(blank=True, null=True)
    collect_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_record'

    def collect_datetime(self):
        return datetime.datetime.fromtimestamp(self.collect_time).strftime("%Y-%m-%d %H:%M:%S")


class NewDevice(models.Model):
    host = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=12, blank=True, null=True)
    ip = models.CharField(max_length=16, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_device'


class OperateLog(models.Model):
    device_name = models.CharField(max_length=16, blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    device_num = models.CharField(max_length=16, blank=True, null=True)
    operation = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operate_log'


class QuanSheng(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    area_num = models.CharField(max_length=8, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    level_nam = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quan_sheng'


class QuanShi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    area_num = models.CharField(max_length=8, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    level_nam = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quan_shi'


class QuanXian(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    area_num = models.CharField(max_length=8, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    level_nam = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quan_xian'


class Rules(models.Model):
    name = models.CharField(max_length=16)
    content = models.TextField()
    comment = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules'


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

    def belong_to_shelf_or_room(self):
        if self.belongto_type == 1:
            return FlowerShelf.objects.get(id=self.belongto_id)
        else:
            return RoomInfo.objects.get(id=self.belongto_id)

    def created_datetime(self):
        return datetime.datetime.fromtimestamp(self.created_time).strftime("%Y-%m-%d %H:%M:%S")


class SensorType(models.Model):
    sensor_type = models.CharField(max_length=16, blank=True, null=True)
    sensor_type_unit = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_type'


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

    def belong_to_shelf_or_room(self):
        if self.belongto_type == 1:
            return FlowerShelf.objects.get(id=self.belongto_id)
        else:
            return RoomInfo.objects.get(id=self.belongto_id)

    def sensor_type(self):
        return SensorType.objects.get(id=self.sensor_type_id)

    def get_last_data(self):
        return DataRecord.objects.filter(sensor_num=self.sensor_num).last()

    def created_datetime(self):
        return datetime.datetime.fromtimestamp(self.created_time).strftime("%Y-%m-%d %H:%M:%S")


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

    def sensors_count(self):
        return SensorInfo.objects.filter(belongto_type=2, belongto_id=self.id).count()

    def relays_count(self):
        return RelayInfo.objects.filter(belongto_type=2, belongto_id=self.id).count()


class SystemDict(models.Model):
    type = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=32, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_dict'


class User(models.Model):
    username = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=255)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
