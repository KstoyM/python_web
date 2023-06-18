from django.shortcuts import render


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

def home_page(request):
    return render(request, 'home-page.html')


def create_profile(request):
    return render(request, 'create-profile.html')


def details_profile(request):
    return render(request, 'profile-details.html')


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')


def catalogue(request):
    return render(request, 'catalogue.html')


def create_plant(request):
    return render(request, 'create-plant.html')


def details_plant(request):
    return render(request, 'plant-details.html')


def edit_plant(request):
    return render(request, 'edit-plant.html')


def delete_plant(request):
    return render(request, 'delete-plant.html')
