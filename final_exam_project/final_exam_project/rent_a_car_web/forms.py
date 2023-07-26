from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Your full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email address'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Subject'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your message here'})