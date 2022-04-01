from django import forms
from profiles.models import Signup

class SignupForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your name'})
    email = forms.CharField(error_messages={'required':'Please enter your email'})
    password = forms.CharField(error_messages={'required':'Please enter your password'})

    class Meta:
        model = Signup
        fields = ('name', 'email', 'password',)