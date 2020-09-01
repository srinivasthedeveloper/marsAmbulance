from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactUs,Booking
from .mail_test import *
from .secure import *

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def news(request):
    return render(request,'news.html')

def contact(request):
    if(request.method=='POST'):
        Name=request.POST['name']
        Phone=request.POST['phonenumber']
        Email=request.POST['mailid']
        Reason=request.POST['reason']
        Message=request.POST['message']

        form=ContactUs.objects.create(name=Name,phoneNo=Phone,emailId=Email,reason=Reason,message=Message)
        form.save()
        SendAnEmail( usrs, psws, fromaddrs, toaddrs, "Contact Form" ,["Name = ","Phone_Number = ","Email_Id = ","Reason = ","Message = "],[Name,Phone,Email,Reason,Message])
        print("form saved")
        return redirect("/")
        
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def portfolio(request):
    return render(request,'portfolio.html')

def pricing(request):
    return render(request,'pricing.html')

def service(request):
    return render(request,'service.html')

def training(request):
    return render(request,'training.html')


def booking(request):
    if(request.method=='POST'):
        dateOfTravelt=request.POST['dateOfTravel']
        timeOfTravelt=request.POST['timeOfTravel']
        patientNamet=request.POST['PatientName']
        sext=request.POST['sex']
        DOBt=request.POST['dateOfBirth']
        ethnicityt=request.POST['Ethnicity']
        riskst=request.POST['risks']
        pickUpAddresst=request.POST['pickupAddress']
        pickUpWardt=request.POST['pickupWard']
        pickUpContactNamet=request.POST['contactnamep']
        pickUpPhoneNOt=request.POST['contactNop']

        destinationAddresst=request.POST['dropAddress']
        destinationWardt=request.POST['dropWard']
        destinationContactNamet=request.POST['dropName']
        destinationPhoneNOt=request.POST['dropphone']

        escortRequirementt=request.POST['escort']
        hcaSext=request.POST['HCA']
        hcaQuantityt=request.POST['HCAQuantity']
        rmnSext=request.POST['RMN']
        rmnQuantityt=request.POST['RMNQuantity']
        rgnSext=request.POST['RGN']
        rgnQuantityt=request.POST['RGNQuantity']

        form=Booking.objects.create(dateOfTravel=dateOfTravelt,   timeOfTravel=timeOfTravelt,  patientName=patientNamet,  sex=sext,  DOB=DOBt,  ethnicity=ethnicityt,    risks=riskst,  pickUpAddress=pickUpAddresst,    pickUpWard=pickUpWardt, pickUpContactName=pickUpContactNamet,   pickUpPhoneNO=pickUpPhoneNOt, destinationAddress=destinationAddresst, destinationWard=destinationWardt, destinationContactName=destinationContactNamet,  destinationPhoneNO=destinationPhoneNOt,   escortRequirement=escortRequirementt,  hcaSex=hcaSext,   hcaQuantity=hcaQuantityt,   rmnSex=rmnSext,    rmnQuantity=rmnQuantityt,    rgnSex=rgnSext, rgnQuantity=rgnQuantityt)
        form.save()
        SendAnEmail( usrs, psws, fromaddrs, toaddrs, "Booking Form" ,["Date of Travel = ","Time of Travel = ","Name of Patient = ","Sex = ","DOB = ","Ethnicity = ","Risks = ","\nPickUp","Address/Hospital = ","Ward/DoorNo = ","Contact Name(at pickup) = ","Phone No(at pickup) = ","\nDestination ","Address/Hospital = ","Ward/DoorNo = ","Contact Name(Destination) = ","Phone No(Destination) = ","Escorts Required = ","(HCA SEX) = ","(HCA Quantity) = ","(RMN SEX) = ","(RMN Quantity) = ","(RGN SEX) = ","(RGN Quantity) = "],[dateOfTravelt,timeOfTravelt,patientNamet,sext,DOBt,ethnicityt,riskst," Details:- \n",pickUpAddresst,pickUpWardt,pickUpContactNamet,pickUpPhoneNOt,"Details:- \n",destinationAddresst,destinationWardt,destinationContactNamet,destinationPhoneNOt,escortRequirementt,hcaSext,hcaQuantityt,rmnSext,rmnQuantityt,rgnSext,rgnQuantityt])
        print("form saved")
        return redirect("/")
    
    return render(request,'booking.html')
