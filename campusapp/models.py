from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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

#extending user models:

class Customer(models.Model):
    user = models.OneToOneField(User,related_name='User',on_delete=models.CASCADE)
    tel_no = models.IntegerField(max_length=14, default=0)

@receiver(post_save, sender=User)
def create_customer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)
        User.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.User.save()
