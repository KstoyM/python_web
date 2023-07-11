from django.shortcuts import render, redirect
from fruitipedia_app.fruitipedia_web.models import ProfileModel, FruitModel
from fruitipedia_app.fruitipedia_web.forms import ProfileCreateForm, ProfileEditForm, FruitCreateForm, \
    FruitEditForm, FruitDeleteForm


# Create your views here.


def get_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist as ex:
        return None


def index_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context=context)


def dashboard_page(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'dashboard.html', context=context)


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'create-fruit.html', context=context)


def details_fruit(request, pk):
    profile = get_profile()
    fruit = FruitModel.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'details-fruit.html', context=context)


def edit_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'edit-fruit.html', context=context)


def delete_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'delete-fruit.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': get_profile(), }

    return render(request, 'create-profile.html', context=context)


def details_profile(request):
    profile = get_profile()
    number_of_posts = FruitModel.objects.count()

    context = {
        'profile': profile,
        'number_of_posts': number_of_posts,
    }

    return render(request, 'details-profile.html', context=context)


def edit_profile(request):

    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index page')

    context = {
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context=context)
