from django import forms
from django.core.exceptions import ValidationError

from .models import ContactUs, Car, RentCar


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


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'car_model', 'price', 'horsepower', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['make'].widget.attrs.update({'placeholder': 'Car make'})
        self.fields['car_model'].widget.attrs.update({'placeholder': 'Car model'})
        self.fields['horsepower'].widget.attrs.update({'placeholder': 'Car horsepower'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Car price'})
        self.fields['image'].widget.attrs.update({'placeholder': 'Car image'})


class RentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = ['date_from', 'date_to']

    def __init__(self, *args, **kwargs):
        self.car = kwargs.pop('car', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')

        if date_from and date_to and self.car:
            overlapping_rentals = RentCar.objects.filter(
                car=self.car,
                date_from__lt=date_to,
                date_to__gt=date_from,
            )

            if overlapping_rentals.exists():
                raise ValidationError("This car is already rented for the selected dates.")

        return cleaned_data

    def save(self, commit=True):
        rent_car = super().save(commit=False)
        rent_car.car = self.car
        if commit:
            rent_car.save()
        return rent_car