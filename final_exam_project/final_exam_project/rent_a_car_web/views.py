from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views import generic as views
from .forms import ContactUsForm, CarForm, RentCarForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic

from .models import Car, RentCar


def index_page(request):
    return render(request, 'index.html')


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


def rents_page(request):
    return render(request, 'rents.html')


def rent_car_view(request, pk):
    print("pk value: ", pk)
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = RentCarForm(request.POST, car=car)
        if form.is_valid():
            form.instance.user = request.user  # Set the user instance for the form
            form.save()

            messages.success(request, f"Car {car.make} has been successfully rented! Total price: {form.cleaned_data['total_price']} EUR")

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
            return redirect('index_page')

        return render(request, self.template_name, {'form': form})


def add_car(request):
    return render(request, 'add_car.html')


1


def add_rent(request):
    return render(request, 'add_rent.html')


def details_rent(request):
    return render(request, 'details_rent.html')


def edit_rent(request):
    return render(request, 'edit_rent.html')


def delete_rent(request):
    return render(request, 'delete_rent.html')
