from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import *

class CustomerForm(ModelForm):
        class Meta:
                model=CustomerModel
                fields='__all__'
                exclude=['user']

class BookingForm(ModelForm):
        class Meta:
                model=Booking
                fields='__all__'

username_validator=UnicodeUsernameValidator()
class CreateUser(UserCreationForm):
        username = forms.CharField(label=_('Username'),max_length=150,help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),validators=[username_validator],error_messages={'unique': _("A user with that username already exists.")},widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter a unique username'}))

        first_name=forms.CharField(label=_('FirstName:'),max_length=100,min_length=2,required=True,help_text='Required: First Name',widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your Firstname'})))        

        last_name=forms.CharField(label=_('LastName:'),max_length=100,min_length=2,required=True,help_text='Required: Last Name',widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your Firstname'})))

        email=forms.EmailField(label=_('Email:'),max_length=200,required=True,help_text='Required: Enter a valid email address',validators=[username_validator],error_messages={'unique':_("A user with that email already exist.")},widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter a valid email'})))

        password1 = forms.CharField(label=_('Password'),widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Please enter password'})),help_text=password_validation.password_validators_help_text_html())

        password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Please repeat password'}),help_text=_('Just Enter the same password, for confirmation'))

        class Meta:
                model = User
                fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
