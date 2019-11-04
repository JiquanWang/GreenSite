# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
