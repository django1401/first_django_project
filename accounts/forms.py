from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'captcha']


class CaptchaForm(forms.Form):
    captcha = CaptchaField()