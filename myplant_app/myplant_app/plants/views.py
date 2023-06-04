from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_page(request):
    profile = ProfileModel.objects.first()
    context = {'profile': profile}

    return render(request, template_name='home-page.html', context=context)


def create(request):
    return HttpResponse("create")


#  catalogue
def catalogue(request):
    return HttpResponse("delete")

