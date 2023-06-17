from django.shortcuts import render, redirect

from games_app.games_web.forms import ProfileForm, GameForm, DeleteGameForm, BaseProfileForm
from games_app.games_web.models import Profile, GameModel


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None


# Create your views here.


def home_page(request):
    profile = get_profile()

    context = {
        "profile": profile,
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    context = {
        'profile': get_profile(),
        'games': GameModel.objects.all(),
    }

    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = GameForm()
    else:
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = GameModel.objects.filter(pk=pk).get()

    context = {
        'game': game,
        'profile': get_profile(),
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    if request.method == 'GET':
        form = GameForm(instance=GameModel.objects.get(pk=pk))

    else:
        form = GameForm(request.POST, instance=GameModel.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    if request.method == 'GET':
        form = DeleteGameForm(instance=GameModel.objects.get(pk=pk))
    else:
        form = DeleteGameForm(request.POST, instance=GameModel.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'delete-game.html', context)


def details_profile(request):
    profile = get_profile()

    total_games = len(GameModel.objects.all())
    average_game_rating = sum([game.rating for game in GameModel.objects.all()]) / total_games if total_games else 0

    context = {
        'profile': profile,
        'total_games': total_games,
        'average_game_rating': average_game_rating,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):

    if request.method == 'GET':
        form = BaseProfileForm(instance=get_profile())

    else:
        form = BaseProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        GameModel.objects.all().delete()
        profile.delete()
        return redirect('home_page')

    context = {
        'profile': get_profile(),
    }

    return render(request, 'delete-profile.html', context)
