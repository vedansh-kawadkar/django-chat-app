from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from rooms.models import Room


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.PasswordInput()
    
    
class CreateRoomForm(forms.Form):
    class Meta:
        model = Room
        fields = ["name", "description", "is_public"]