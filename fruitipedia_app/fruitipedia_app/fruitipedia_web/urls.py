from django.urls import path, include
from .views import index_page, dashboard_page, create_fruit, details_fruit, edit_fruit, delete_fruit, \
    create_profile, details_profile, edit_profile, delete_profile


urlpatterns = [
    path('', index_page, name='index page'),
    path('dashboard/', dashboard_page, name='dashboard page'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', details_fruit, name='details fruit'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit')
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ]))
]