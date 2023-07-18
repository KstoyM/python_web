from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
