from django.shortcuts import render, redirect

from library_app.library_web.forms import ProfileCreateForm
from library_app.library_web.models import Profile


# •	http://localhost:8000/ - home page
# •	http://localhost:8000/add/ - add book page
# •	http://localhost:8000/edit/:id - edit book page
# •	http://localhost:8000/details/:id - book details page
# •	http://localhost:8000/profile/ - profile page
# •	http://localhost:8000/profile/edit/ - edit profile page
# •	http://localhost:8000/profile/delete/ - delete profile page


# Create your views here.

def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None

def home_page(request):
    profile = get_profile()

    if profile is None:
        return profile_register(request)

    return render(request, 'home-with-profile.html')

def add_book(request):
    return render(request, 'add-book.html')

def edit_book(request, pk):
    return render(request, 'edit-book.html')

def details_book(request, pk):
    return render(request, 'book-details.html')

def profile_page(request):
    return render(request, 'profile.html')

def profile_register(request):

    if get_profile() is not None:
        return redirect('home-with-profile.html')

    # if request.method == 'GET':
    #     form = ProfileCreateForm()
    # else:
    #     form = ProfileCreateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home-with-profile.html')

    # context = {
    #     'form': form,
    #     'hide_nav_links': True,
    # }

    return render(request, 'home-no-profile.html')

def edit_profile(request):
    return render(request, 'edit-profile.html')

def delete_profile(request):
    return render(request, 'delete-profile.html')
