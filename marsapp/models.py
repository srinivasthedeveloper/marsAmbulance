from django.db import models

class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    phoneNo=models.CharField(max_length=13)
    emailId=models.CharField(max_length=220)
    message=models.TextField(max_length=10000)
    reason=models.CharField(max_length=400)
    date_Created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+'-->'+self.reason+'-->'+str(self.date_Created)


class Booking(models.Model):
    dateOfTravel=models.CharField(max_length=15,null=True,blank=True)
    timeOfTravel=models.CharField(max_length=15,null=True,blank=True)
    patientName=models.CharField(max_length=400,null=True,blank=True)
    sex=models.CharField(max_length=10,null=True,blank=True)
    DOB=models.CharField(max_length=15,null=True,blank=True)
    ethnicity=models.CharField(max_length=20,null=True,blank=True)
    risks=models.CharField(max_length=1000,null=True,blank=True)
    pickUpAddress=models.TextField(max_length=1000,null=True,blank=True)
    pickUpWard=models.CharField(max_length=100,null=True,blank=True)
    pickUpContactName=models.CharField(max_length=200,null=True,blank=True)
    pickUpPhoneNO=models.CharField(max_length=15,null=True,blank=True)
    
    destinationAddress=models.TextField(max_length=1000,null=True,blank=True)
    destinationWard=models.CharField(max_length=100,null=True,blank=True)
    destinationContactName=models.CharField(max_length=200,null=True,blank=True)
    destinationPhoneNO=models.CharField(max_length=15,null=True,blank=True)

    escortRequirement=models.CharField(max_length=10,null=True,blank=True)
    hcaSex=models.CharField(max_length=30,null=True,blank=True)
    hcaQuantity=models.CharField(max_length=30,null=True,blank=True)
    rmnSex=models.CharField(max_length=30,null=True,blank=True)
    rmnQuantity=models.CharField(max_length=30,null=True,blank=True)
    rgnSex=models.CharField(max_length=30,null=True,blank=True)
    rgnQuantity=models.CharField(max_length=30,null=True,blank=True)
    
    date_Created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.patientName+'-->'+self.sex+'-->'+self.risks+'-->'+str(self.dateOfTravel)
