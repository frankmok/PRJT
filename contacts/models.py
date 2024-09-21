from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing_brand = models.CharField(max_length=100)
    listing_model = models.CharField(max_length=100)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
