from django.db import models
from datetime import datetime

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255)
    upid = models.IntegerField()

    class Meta:
        db_table = 'district'
    
class Users(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=20)
    createTime = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = "users"  # 指定表名