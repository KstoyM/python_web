from django.urls import path, include
from .views import index_page, rents_page, ContactPageView, AddCars, \
    add_rent, details_rent, edit_rent, delete_rent, CarsPageView, rent_car_view

urlpatterns = [

    path('', index_page, name='index_page'),

    path('add_cars/', AddCars.as_view(), name='add_cars'),

    path('catalogue/', include([
        path('', CarsPageView.as_view(), name='catalogue_page'),
        path('rent_car_view/<int:pk>/', rent_car_view, name='rent_car_view'),
    ])),

    path('rents/', include([
        path('', rents_page, name='rents_page'),
        path('details/<int:pk>/', details_rent, name='details_rent'),
        path('edit/<int:pk>/', edit_rent, name='edit_rent'),
        path('delete/<int:pk>/', delete_rent, name='delete_rent'),
    ])),

    path('contact/', ContactPageView.as_view(), name='contact_page'),
]
