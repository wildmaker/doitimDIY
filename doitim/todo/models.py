from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    """用户新增的事务"""
    desc = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    start_date = models.DateTimeField(null = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.desc