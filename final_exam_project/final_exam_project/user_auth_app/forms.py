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
        fields = ('username', 'email', 'age', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
            'age': 'Age',
        }


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('old_password', 'new_password1', 'new_password2')
        labels = {
            'old_password': 'Old Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm New Password',
        }
