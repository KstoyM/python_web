from django.shortcuts import render
import random


# Create your views here.

def index(request):
    context = {
        "title": "Home",
        "random_int": random.random
    }

    return render(request, "examples_templates/index.html", context=context)
