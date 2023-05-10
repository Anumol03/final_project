from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["email","username","password1","password2"]
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class PasswordResetForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label="new password", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="confirm new password", widget=forms.PasswordInput(attrs={"class":"form-control"}))