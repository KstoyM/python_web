from .views import create, details, edit, delete
from django.urls import path, include

urlpatterns = [
    path('profile/', include([
        path('create/', create, name='profile-create-page'),
        path('details/', details, name='profile-details-page'),
        path('edit/', edit, name='profile-edit-page'),
        path('delete/', delete, name='profile-delete-page'),
    ]))
]
