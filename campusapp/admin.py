from django.contrib import admin
from django.apps import apps
import models
from django.contrib.auth.models import User



# Register your models here.
#admin.site.unregister(User) @TODO fix this so can edit user FROM customer edit. ... lol i fixed it and i dont know how.

admin.site.register(models.Event)
admin.site.register(models.Promotion)
admin.site.register(models.Item)
admin.site.register(models.FoodItem)
admin.site.register(models.DrinkItem)
admin.site.register(models.Customer)
