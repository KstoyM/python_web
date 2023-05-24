from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse


# Create your views here.

def index(request):
    print(request)
    return HttpResponse("index")


def details(request, department_id):
    departments_map = {
        '1': 'Developers',
        '2': 'QA'
    }

    payload = f'Department: {departments_map.get(str(department_id), "Unknown")}'

    return HttpResponse(payload)


def details_template(request, department_id):
    departments_map = {
        '1': 'Developers',
        '2': 'QA'
    }

    payload = f'Department: {departments_map.get(str(department_id), "Unknown")}'

    context = {
        "title": "Departments title from context",
        "payload": payload
    }

    return render(request, 'departments/details.html', context=context)

def details_error(request, department_id):
    return HttpResponse("error")