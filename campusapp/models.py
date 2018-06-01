from django.db import models



# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    datetime = models.DateTimeField()
    price = models.FloatField(default=00.00)
    #image = models.ImageField(upload_to="campusapp/images/", default=None)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.name

class Promotion(models.Model):
    #put in offer ID and times redeemed field.
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    image = models.ImageField(default=None)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    description =models.TextField(max_length=200)
    price = models.FloatField(default=00.00)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    MenuItem = models.OneToOneField(MenuItem)  #extends Menu Item (does this work?)
    SideItem = models.OneToManyField(SideItem) #might need to change order of this as SideItem defined afterwards

    def __str__(self):
        return self.name

class SideItem(models.Model):
    name = models.CharField(max_length=30)
    Quantity = models.IntegerField(default = 0)
    image = models.ImageField(default=None) #might need to remove this later - extending class with image FloatField

    def __str__(self):
        return self.name
