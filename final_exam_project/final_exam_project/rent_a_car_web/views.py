from django.shortcuts import render

# Create your views here.
# urlpatterns = [
#     path('', index_page, name='index page'),
#
#     path('cars/', include([
#         path('', cars_page, name='cars page'),
#         path('cars/add/', add_car, name='add car'),
#         path('cars/details/<int:pk>/', details_car, name='details car'),
#         path('cars/edit/<int:pk>/', edit_car, name='edit car'),
#         path('cars/delete/<int:pk>/', delete_car, name='delete car'),
#     ])),
#
#     path('rents/', include([
#         path('', rents_page, name='rents page'),
#         path('rents/add/', add_rent, name='add rent'),
#         path('rents/details/<int:pk>/', details_rent, name='details rent'),
#         path('rents/edit/<int:pk>/', edit_rent, name='edit rent'),
#         path('rents/delete/<int:pk>/', delete_rent, name='delete rent'),
#     ])),
#
#
#     path('contact/', contact_page, name='contact page'),
#     path('about/', about_page, name='about page'),
# ]


def index_page(request):
    return render(request, 'index.html')

def cars_page(request):
    return render(request, 'cars.html')

def rents_page(request):
    return render(request, 'rents.html')

def contact_page(request):
    return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')

def add_car(request):
    return render(request, 'add_car.html')

def details_car(request):
    return render(request, 'details_car.html')

def edit_car(request):
    return render(request, 'edit_car.html')

def delete_car(request):
    return render(request, 'delete_car.html')

def add_rent(request):
    return render(request, 'add_rent.html')

def details_rent(request):
    return render(request, 'details_rent.html')

def edit_rent(request):
    return render(request, 'edit_rent.html')

def delete_rent(request):
    return render(request, 'delete_rent.html')

