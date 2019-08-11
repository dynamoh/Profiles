from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')




class ProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ('name','college','age','gender','dateOfBirth','image')
