from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.Logout,name='logout'),


    path('newbooking/',views.newbooking,name='newbooking'),
    path('updatebooking/<str:pk>/',views.updatebooking,name='updatebooking'),
    path('deletebooking/<str:pk>/',views.deletebooking,name='deletebooking'),

]
