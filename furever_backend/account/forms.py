from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, ShelterProfile

class SignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ('email', 'name', 'password1', 'password2',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'avatar',)

class ShelterProfileForm(forms.ModelForm):
    class Meta:
        model = ShelterProfile
        fields = ('workers', 'animals')
