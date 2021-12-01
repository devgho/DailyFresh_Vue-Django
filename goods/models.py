from datetime import datetime

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='goods/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    add_time = models.DateTimeField(default=datetime.now)
    click_num = models.IntegerField(default=0)
    brief = models.CharField(max_length=500,default="暂无商品信息描述")

    def __str__(self):
        return self.name