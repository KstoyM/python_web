from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileCreateForm
from my_music_app.web.models import Profile

# Create your views here.
'''
• http://localhost:8000/profile/details/ - profile details page
• http://localhost:8000/profile/delete/ - delete profile page'''


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def home_page(request):
    profile = get_profile()

    if profile is None:
        return redirect('add profile')

    return render(request, 'home-with-profile.html')


def add_album(request):
    return render(request, 'add-album.html')


def details_album(request, pk):
    return render(request, 'album-details.html')


def edit_album(request, pk):
    return render(request, 'edit-album.html')


def delete_album(request, pk):
    return render(request, 'delete-album.html')


def details_profile(request):
    return render(request, 'profile-details.html')


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    return render(request, 'profile-delete.html')
