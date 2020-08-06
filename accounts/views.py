from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomerModel,Tag,AmbulanceType,Booking
from .forms import CustomerForm,BookingForm,CreateUser
from .decorators import unauthendicated_user

# Create your views here.

@unauthendicated_user
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Incorrect username or password')
            
    return render(request,'signin.html')

@unauthendicated_user
def signup(request):
    form=CreateUser()
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')


            '''            
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            CustomerModel.objects.create(
            user=user,
            name=user.username,
            )
            print('Profile created!')
            '''


            messages.success(request,username+" Created")
            return redirect('signin')
    data={
        'form':form
        }    
    return render(request,'signup.html',data)

def Logout(request):
    logout(request)
    return redirect('signin')



def newbooking(request):
    form=BookingForm()
    booking=Booking.objects.all()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data={'form':form,'booking':booking}
    return render(request,'newbooking.html',data)

def updatebooking(request,pk):
    booking=Booking.objects.get(id=pk)
    form=BookingForm(instance=booking)
    if request.method=='POST':
        form=BookingForm(request.POST,instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/')
    data={'form':form,'booking':booking}
    return render(request,'updatebooking.html',data)

def deletebooking(request,pk):
    booking=Booking.objects.get(id=pk)
    #if request.method=='POST':
    booking.delete()
    return redirect('/')
