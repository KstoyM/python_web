from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def create(request):
    return HttpResponse('profile create')


def details(request):
    return HttpResponse('profile details')


def edit(request):
    return HttpResponse('profile edit')


def delete(request):
    return HttpResponse('profile delete')
