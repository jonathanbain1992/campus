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

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=00.00)
    description = models.TextField(max_length=200)
    price = models.FloatField(default=00.00)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    Item = models.ForeignKey(Item)
    def __str__(self):
        return self.Item.name

class DrinkItem(models.Model):
    CHOICES = (
    (330, '330ml'),
    (660,'660ml'),
    (284,'half pint'),
    (568,'pint'),
    (1136,'2 pint pitcher'),
    )
    Quantity = models.IntegerField(choices = CHOICES, max_length=20, default="")
    Item = models.ForeignKey(Item)
    def __str__(self):
        return self.Item.name
