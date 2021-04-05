from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder': 'Kullanıcı Adı',
    }))
    password = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifre',
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder': 'Kullanıcı Adı',
    }))
    password1 = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifre',
    }))
    password2 = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifre Doğrulama',
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']