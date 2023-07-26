from django.urls import path, include
from .views import index_page, cars_page, rents_page, ContactPageView, \
    add_car, details_car, edit_car, delete_car, add_rent, details_rent, edit_rent, delete_rent

urlpatterns = [

    path('', index_page, name='index_page'),

    path('cars/', include([
        path('', cars_page, name='cars_page'),
        path('cars/add/', add_car, name='add_car'),
        path('cars/details/<int:pk>/', details_car, name='details_car'),
        path('cars/edit/<int:pk>/', edit_car, name='edit_car'),
        path('cars/delete/<int:pk>/', delete_car, name='delete_car'),
    ])),

    path('rents/', include([
        path('', rents_page, name='rents_page'),
        path('rents/add/', add_rent, name='add_rent'),
        path('rents/details/<int:pk>/', details_rent, name='details_rent'),
        path('rents/edit/<int:pk>/', edit_rent, name='edit_rent'),
        path('rents/delete/<int:pk>/', delete_rent, name='delete_rent'),
    ])),

    path('contact/', ContactPageView.as_view(), name='contact_page'),
]
