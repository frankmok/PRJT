from django.db import models
from brokers.models import Broker

# Create your models here.
class Listing(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    four_or_two_doors = models.BooleanField(default=True)
    seats = models.IntegerField()
    milage = models.DecimalField(max_digits=6, decimal_places=1)
    range = models.DecimalField(max_digits=4, decimal_places=1)
    right_or_left_hand_drive = models.BooleanField(default=True)
    four_or_two_wheels_drive = models.BooleanField(default=True)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.brand + '. ' + self.model
