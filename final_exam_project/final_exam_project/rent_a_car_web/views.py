from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm
from django.contrib import messages


def index_page(request):
    return render(request, 'index.html')


def cars_page(request):
    return render(request, 'cars.html')


def rents_page(request):
    return render(request, 'rents.html')


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


def about_page(request):
    return render(request, 'about.html')


def add_car(request):
    return render(request, 'add_car.html')


def details_car(request):
    return render(request, 'details_car.html')


def edit_car(request):
    return render(request, 'edit_car.html')


def delete_car(request):
    return render(request, 'delete_car.html')


def add_rent(request):
    return render(request, 'add_rent.html')


def details_rent(request):
    return render(request, 'details_rent.html')


def edit_rent(request):
    return render(request, 'edit_rent.html')


def delete_rent(request):
    return render(request, 'delete_rent.html')
