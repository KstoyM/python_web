from urllib import request
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import ContactUsForm, CarForm, RentCarForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic as views
from .models import Car, RentCar
from .. import settings


def index_page(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'index.html', context=context)


class AddCars(UserPassesTestMixin, views.CreateView):
    template_name = 'add_cars.html'
    form_class = CarForm
    model = Car
    success_url = reverse_lazy('index_page')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def form_valid(self, form):
        messages.success(self.request, 'Car added successfully!')
        return super().form_valid(form)


class CarsPageView(View):
    template_name = 'catalogue_page.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars': cars})


def rent_car_view(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = RentCarForm(request.POST, car=car)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return redirect('index_page')

    return redirect('catalogue_page')


class ContactPageView(View):
    template_name = 'contact_page.html'

    def get(self, request):
        form = ContactUsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            from_email = email if email else settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]
            message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            return redirect('index_page')

        return render(request, self.template_name, {'form': form})


def rent_history(request, pk):

    rents_history = RentCar.objects.filter(user_id=pk)

    context = {
        'rents_history': rents_history,
    }

    return render(request, 'rents_history.html', context=context)


def edit_rent(request):
    return render(request, 'edit_rent.html')


class DeleteRentView(views.DeleteView):
    pass
