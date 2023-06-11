# Create your views here.

from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm
from car_collection_app.web.models import Profile, Car


# def get_profile():
#     try:
#         return Profile.objects.get()
#     except Profile.DoesNotExist as ex:
#         return None


def index(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, 'index.html', context=context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context=context)


def catalogue(request):
    profile = Profile.objects.first()
    car_count = Car.objects.count()
    cars = Car.objects.all()

    context = {
        'profile': profile,
        'cars': cars,
        'car_count': car_count,
    }

    return render(request, 'catalogue.html', context=context)


def car_create(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'car-create.html', context=context)


def car_details(request, pk):
    car = Car.objects.get(id=pk)
    context = {
        'profile': Profile.objects.first(),
        'car': car
    }

    return render(request, template_name='car-details.html', context=context)


def car_edit(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(id=pk)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'car-edit.html', context=context)


def car_delete(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            car.delete()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
        'car': car,
    }

    return render(request, 'car-delete.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    total_cars_value = sum([car.price for car in Car.objects.all()])
    context = {
        'profile': profile,
        'total_cars_value': total_cars_value,
    }

    return render(request, 'profile-details.html', context=context)


def profile_edit(request):
    if request.method == 'GET':
        form = ProfileEditForm(instance=Profile.objects.first())
    else:
        form = ProfileEditForm(request.POST, instance=Profile.objects.first())
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        "form": form,
        "profile": Profile.objects.first(),
    }

    return render(request, 'profile-edit.html', context=context)


def profile_delete(request):
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index_page')
