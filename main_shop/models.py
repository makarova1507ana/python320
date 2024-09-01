from django.db import models


class News(models.Model):
    '''
    поля класса -> это его атрибуты в таблице БД
    create News(
        title TEXT(title <= 25),
        description TEXT,
        image BLOB
    );
    title - заголовок
    '''
    title = models.CharField(max_length=25) # максимум 25 симолов
    description = models.TextField() # неопределенной длины

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.IntegerField()
