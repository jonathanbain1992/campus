from django.conf.urls import include, url
from django.conf import settings
from campusapp.views import *
from django.conf.urls.static import static






urlpatterns = [
    # Examples:
    # url(r'^$', 'Campus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^account', include('account.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^menu/food', FoodMenu.as_view(), name='foodmenu'),
    url(r'^menu/drink', DrinkMenu.as_view(), name='drinkmenu'),
    url(r'^register', RegisterUserView.as_view(),name='register'),
    url(r'^register_customer', RegisterCustomerView.as_view(),name='registercustomer'),


    ]
