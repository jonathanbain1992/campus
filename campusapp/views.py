from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from campusapp.models import *
from django.db.models import Q
import datetime


# Create your views here.

class Index(View):
    template = "default.html"
#    @TODO: check this works with server out of development mode - only seems to refresh when server restarted just now
#    @TODO: parametarise this so that the admin can decide the 'grace period' for displaying an event PER event
#    @TODO: filter by subcategory once i have an idea of what these are perhaps, or could delegate to child class model.
    allEvents = Event.objects.filter(Q(datetime__gt=datetime.datetime.now()), Q(datetime__lt=(datetime.datetime.now()+datetime.timedelta(days=7)))).order_by('datetime')
    context = {"events":allEvents}
    def get(self,request):

        return render(request,self.template,self.context)
