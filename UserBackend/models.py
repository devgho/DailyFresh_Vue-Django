from django.db import models
from goods.models import Good
from datetime import datetime
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=20, default='')
    post_code = models.CharField(max_length=20, default='')
    receiver = models.CharField(max_length=10, default='')
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nums = models.IntegerField()
    good = models.ForeignKey(Good, on_delete=models.CASCADE)