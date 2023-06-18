from django.urls import path, include
from .views import home_page, add_book, edit_book, details_book, profile_page, edit_profile, delete_profile


urlpatterns = [
    path('', home_page, name='home_page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('profile/', include([
        path('', profile_page, name='profile page'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ]))
]

