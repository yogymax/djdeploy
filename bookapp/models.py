from django.db import models


class Book(models.Model):
    bookname = models.CharField(max_length=100)
    bookprice = models.FloatField()
    bookqty = models.IntegerField()
    bookauthor = models.CharField(max_length=100)
    bookcate = models.CharField(max_length=100)
    active = models.CharField(max_length=10,default='Y')
    class Meta:
        db_table='Book_Info'
