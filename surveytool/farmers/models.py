from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    land_area = models.FloatField(default=0.0)
    water_area = models.FloatField(default=0.0)
    reg_number = models.CharField(max_length=50)
    farm_location = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=11)
