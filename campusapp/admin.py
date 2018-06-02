from django.contrib import admin
from django.apps import apps
import models



# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Promotion)
admin.site.register(models.Item)
admin.site.register(models.FoodItem)
admin.site.register(models.DrinkItem)
