from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

# Create your models here.

# model for customer

class CustomerModel(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phoneNo=models.CharField(max_length=13,null=True)
    emailId=models.CharField(max_length=220,null=True)
    address=models.TextField(max_length=1000,null=True)
    profilePic=models.ImageField(default="",null=True,blank=True)
    date_Created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=144,null=True)

    def __str__(self):
        return self.name

class AmbulanceType(models.Model):
    tags=models.ManyToManyField(Tag)
    CATEGORY=(
        ('NormalAmbulance','NormalAmbulance'),
        ('SecureAmbulance','SecureAmbulance'),
        ('HighSecureAmbulance','HighSecureAmbulance'),
        ('Ambulance<->Young&Child','Ambulance<->Young&Child'),
        ('WheelchairAmbulance','WheelchairAmbulance'),
        )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.TextField(null=True,blank=True)
    date_Created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customers=models.ForeignKey(CustomerModel,null=True,on_delete=models.SET_NULL)
    bookedAmbulance=models.ForeignKey(AmbulanceType,null=True,on_delete=models.SET_NULL)
    STATUS=(
        ('Served','Served'),
        ('Pending','Pending'),
        ('Out of Order','Out of Order'),
        )
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    TYPE=(
        ('Emergency','Emergency'),
        ('Pre-Booking','Pre-Booking'),
        )
    bookingType=models.CharField(max_length=100,null=True,choices=TYPE)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.customers.name+'->'+self.bookedAmbulance.name+'->'+self.status
