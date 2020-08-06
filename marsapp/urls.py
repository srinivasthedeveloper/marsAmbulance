from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('service/',views.service,name='service'),
    path('training/',views.training,name='training'),
    path('booking/',views.booking,name='booking'),    

]

