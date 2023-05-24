from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "title": "Home",
    }
    return render(request, 'templates/examples_templates/index.html', context=context)
