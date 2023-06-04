from .views import create, details, edit, delete
from django.urls import path, include

urlpatterns = [
    path('profile/', include([
        path('create/', create, name='create-profile'),
        path('details/', details, name='profile-details'),
        path('edit/', edit, name='edit-profile'),
        path('delete/', delete, name='delete-profile'),
    ]))
]
