from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfForm(forms.ModelForm):
    class Meta:
        model = UserProfInfo
        fields = ('portfolio','profile_pic')
