from django import forms
from django.core.validators import EmailValidator

class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Password', max_length=48, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    remember = forms.BooleanField(label='Remember Me', required=False)
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    second_name = forms.CharField(label='Second Name', max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия(необязательно)'}))
    login = forms.CharField(label='Login', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', max_length=48, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=48, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    re_password = forms.CharField(label='Repeat password', max_length=48, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    
