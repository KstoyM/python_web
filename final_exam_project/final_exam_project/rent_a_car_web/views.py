from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
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
        return self.request.user.groups.filter(Q(name='Superuser') | Q(name='Is_Staff')).exists()

    def form_valid(self, form):
        messages.success(self.request, 'Car added successfully!')
        return super().form_valid(form)


def are_dates_valid(date_from, date_to):
    try:
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = datetime.strptime(date_to, '%Y-%m-%d')
    except ValueError:
        return False

    return date_to > date_from


class CarsPageView(View):
    template_name = 'catalogue_page.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars': cars})


def rent_car_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    user_pk = request.user.pk

    if request.method == 'POST':
        form = RentCarForm(request.POST, car=car)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            messages.success(request, 'Car rented successfully.')

            redirect_url = reverse('rents_history', kwargs={'pk': user_pk})
            return redirect(redirect_url)

    return render(request, 'catalogue_page.html', {'cars': Car.objects.all(), 'form': RentCarForm()})


def check_car_availability(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        try:
            car = Car.objects.get(pk=car_id)
            if car.is_car_rented(date_from, date_to):
                return JsonResponse({'available': False, 'error': 'This car is already rented for the selected dates.'})
            else:
                return JsonResponse({'available': True})
        except Car.DoesNotExist:
            return JsonResponse({'available': False, 'error': 'Invalid car ID.'})

    return JsonResponse({'available': False, 'error': 'Invalid request method.'})


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


@login_required
def rent_history(request, pk):
    if request.user.pk != pk:
        return HttpResponseForbidden("You don't have permission to access this page.")

    rents_history = RentCar.objects.filter(user_id=pk)

    for rent in rents_history:
        rent.duration = (rent.date_to - rent.date_from).days
        rent.total_price = rent.duration * rent.car.price

    paginator = Paginator(rents_history, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'rents_history.html', context=context)


class DeleteRentView(views.DeleteView):
    model = RentCar
    success_url = reverse_lazy('index_page')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Rent deleted successfully!')
        return super().delete(request, *args, **kwargs)
