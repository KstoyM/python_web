from django import forms

from library_app.library_web.models import Book, Profile


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'