from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.conf import settings

# Create your models here.


class ListingManager(models.Manager):
    def all(self):
        return super(ListingManager, self).filter(is_published=True)


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=160)
    address = models.CharField(max_length=160)
    city = models.CharField(max_length=160)
    state = models.CharField(max_length=160)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.DecimalField(max_digits=10, decimal_places=2)
    lot_size = models.DecimalField(max_digits=10, decimal_places=2)
    photo_main = models.ImageField(upload_to='images/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    photo_2 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    photo_3 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    photo_4 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    photo_5 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    photo_6 = models.ImageField(upload_to='images/%y/%m/%d/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    objects = ListingManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-list_date"]
