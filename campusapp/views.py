from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import CreateView
from django.views.generic.base import View
from campusapp.models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
import datetime
from forms import *


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

class FoodMenu(View):
    template="Menu.html"
    allMenuItems = FoodItem.objects.all()
    context = {"items": allMenuItems}

    def get(self,request):
        return render(request,self.template,self.context)


class DrinkMenu(View):
    template="Menu.html"
    allMenuItems = DrinkItem.objects.all()
    context = {"items": allMenuItems}

    def get(self,request):
        return render(request,self.template,self.context)


#user authentication

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"

  # @override
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        if form.is_valid():
            pw = form.cleaned_data['password']
            pw2 = form.cleaned_data['password2']
            if pw != pw2:
                return ValidationError("passwords do not match")
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                return HttpResponse("success")

class RegisterCustomerView(CreateView):
    form_class = RegisterCustomerForm
    template_name = "register.html"

  # @override
    def dispatch(self,request,*args,**kwargs):
        if request.Customer.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterCustomerView, self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        if form.is_valid():
            pw = form.cleaned_data['password']
            pw2 = form.cleaned_data['password2']
            if pw != pw2:
                return ValidationError("passwords do not match")
            else:
                user = form.save(commit=False)
                Customer.set_password(form.cleaned_data['password'])
                Customer.save()
                return HttpResponse("success")
