from django.shortcuts import render, redirect
from plants_app.plants_web.forms import ProfileForm, PlantBaseForm, PlantDeleteForm, ProfileBaseForm
from plants_app.plants_web.models import ProfileModel, PlantModel


# •	http://localhost:8000/ - home page
# •	http://localhost:8000/profile/create/ - profile create page
# •	http://localhost:8000/catalogue/ - catalogue
# •	http://localhost:8000/create/ - plant create page
# •	http://localhost:8000/details/<plant_id>/ - plant details page
# •	http://localhost:8000/edit/<plant_id>/ - plant edit page
# •	http://localhost:8000/delete/<plant_id>/ - plant delete page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/ - profile delete page

# Create your views here.

def get_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist as ex:
        return None


def home_page(request):
    if get_profile():
        context = {
            'profile': get_profile(),
        }
        return render(request, 'home-page.html', context=context)

    return render(request, 'home-page.html')


def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context=context)


def details_profile(request):
    stars_count = PlantModel.objects.all().count()

    profile = get_profile()
    context = {
        'profile': profile,
        'stars_count': stars_count,
    }
    return render(request, 'profile-details.html', context=context)


def edit_profile(request):
    if request.method == 'GET':
        form = ProfileBaseForm(instance=get_profile())
    else:
        form = ProfileBaseForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()

        return redirect('home_page')

    context = {
        'profile': profile
    }

    return render(request, 'delete-profile.html', context=context)


def catalogue(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'catalogue.html', context=context)


def create_plant(request):
    profile = get_profile()

    if request.method == 'GET':
        form = PlantBaseForm()
    else:
        form = PlantBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile:': profile,
        'form': form,
    }

    return render(request, 'create-plant.html', context=context)


def details_plant(request, pk):
    plant = PlantModel.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
        'profile': get_profile(),
    }

    return render(request, 'plant-details.html', context=context)


def edit_plant(request, pk):
    if request.method == 'GET':
        form = PlantBaseForm(instance=PlantModel.objects.filter(pk=pk).get())
    else:
        form = PlantBaseForm(request.POST, instance=PlantModel.objects.filter(pk=pk).get())
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'edit-plant.html', context=context)


def delete_plant(request, pk):
    if request.method == 'GET':
        form = PlantDeleteForm(instance=PlantModel.objects.filter(pk=pk).get())
    else:
        form = PlantDeleteForm(request.POST, instance=PlantModel.objects.filter(pk=pk).get())
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'delete-plant.html', context=context)
