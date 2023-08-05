from django.urls import path, include
from .views import index_page, ContactPageView, AddCars, \
    edit_rent, DeleteRentView, CarsPageView, rent_car_view, rent_history, check_car_availability

urlpatterns = [

    path('', index_page, name='index_page'),

    path('add_cars/', AddCars.as_view(), name='add_cars'),

    path('catalogue/', include([
        path('', CarsPageView.as_view(), name='catalogue_page'),
        path('rent_car_view/<int:pk>/', rent_car_view, name='rent_car_view'),
        path('check_car_availability/', check_car_availability, name='check_car_availability'),
    ])),

    path('rent_history/<int:pk>/', rent_history, name='rents_history'),
    path('edit_rent/<int:pk>/', edit_rent, name='edit_rent'),
    path('delete_rent/<int:pk>/', DeleteRentView.as_view(), name='delete_rent'),

    path('contact/', ContactPageView.as_view(), name='contact_page'),

]
