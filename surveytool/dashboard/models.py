from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=50)
    land_area = models.FloatField(default=0.0) # radius for now
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    is_diseased = models.BooleanField(default=False)
    phone = models.CharField(max_length=11)

    def __str__(self):
    	return str({'name':self.name,
    	'land_area':self.land_area,
    	'latitude':self.latitude,
    	'longitude':self.longitude,
    	'is_diseased':self.is_diseased})

class RealFarmer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    land_area = models.FloatField(default=0.0) # radius for now
    water_area = models.FloatField(default=0.0)
    reg_number = models.CharField(max_length=50)
    farm_location = models.CharField(max_length=250)

