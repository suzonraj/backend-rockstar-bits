from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# SignUp Form.
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, help_text='',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=False, help_text='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=50, required=False, help_text='', label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=10, required=False, help_text='', label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
