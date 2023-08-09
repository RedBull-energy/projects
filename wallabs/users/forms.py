from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Your username", widget=forms.TextInput(attrs={'class': 'auth-input'}))
    password = forms.CharField(label="Your password", widget=forms.PasswordInput(attrs={'class': 'auth-input'}))


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', label="Enter email",
                             widget=forms.TextInput(attrs={'class': 'auth-input'}))
    group = forms.ChoiceField(choices=((1, "Comedy"), (2, "Drama"), (3, "Detective"), (4, "Cartoons"), (5, "Anime")), help_text='group')
    username = forms.CharField(max_length=20, help_text='nickname', label="Choose a nickname",
                               widget=forms.TextInput(attrs={'class': 'auth-input'}))
    password1 = forms.CharField(max_length=20, label="Imagine a password",
                                widget=forms.PasswordInput(attrs={'class': 'auth-input'}))
    password2 = forms.CharField(max_length=20, label="Repeat your password",
                                widget=forms.PasswordInput(attrs={'class': 'auth-input'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'group')


