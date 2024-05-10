from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    first_name = forms.CharField(
        label='First Name',
        help_text='Enter your first name.',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter First Name"
        })
    )

    last_name = forms.CharField(
        label='Last Name',
        help_text='Enter your last name.',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Last Name"
        })
    )

    username = forms.CharField(
        label='Username',
        help_text='This will be your unique username.',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Username"
        })
    )

    email = forms.EmailField(
        label='Email',
        help_text='Enter your email address.',
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Email"
        })
    )

    password1 = forms.CharField(
        label='Password',
        help_text='Your password must contain at least 8 characters.',
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Password"
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        help_text='Enter the same password as above, for verification.',
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
    )

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "id": "Username",
        "class": "form-control",
        "placeholder": "Enter Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "id": "Password",
        "class": "form-control",
        "placeholder": "Password"
    }))