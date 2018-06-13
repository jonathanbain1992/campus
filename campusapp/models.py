from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

#extending user models:



class Customer(models.Model):
    user = models.OneToOneField(User,related_name='User',on_delete=models.CASCADE)
    tel_no = models.IntegerField(default=0)
    image = models.ImageField(default=None)
    niftyfiftypts = models.IntegerField(default=0)
    #drinkspurchases = models.ForeignKey(DrinkItem)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_customer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)
    #    User.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.User.save()






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

    name = models.CharField(max_length=30, default=None)
    price = models.FloatField(default=None)
    description = models.TextField(max_length=200, default=None)
    price = models.FloatField(default=None)
    image = models.ImageField(default=None)

    class Meta:
        abstract = True






class FoodItem(Item):
    CHOICES =(
    (0,"small"),
    (0,"medium"),
    (0, "large"),
    )

    size = models.IntegerField(choices= CHOICES, default=0)

    def __str__(self):
        return self.name

class DrinkItem(Item):
    CHOICES = (
    (330, '330ml'),
    (660,'660ml'),
    (284,'half pint'),
    (568,'pint'),
    (1136,'2 pint pitcher'),
    )
    Quantity = models.IntegerField(choices = CHOICES, default=0)




    def __str__(self):
        return self.name

class Order(models.Model):
    localDateTime = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    FoodItem = models.ManyToManyField(FoodItem, default=None)
    DrinkItem = models.ManyToManyField(DrinkItem, default=None)
    list_display=('localDateTime')

    def __str__(self):
        return str(self.localDateTime)
