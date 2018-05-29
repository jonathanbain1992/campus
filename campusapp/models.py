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
