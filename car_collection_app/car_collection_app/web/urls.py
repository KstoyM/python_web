from django.urls import path, include
from .views import index, catalogue, profile_create, profile_details, profile_edit, profile_delete, car_create, \
    car_details, car_edit, car_delete

# •	http://localhost:8000/ - index page
# •	http://localhost:8000/profile/create - profile create page
# •	http://localhost:8000/catalogue/ - catalogue page
# •	http://localhost:8000/car/create/ - car create page
# •	http://localhost:8000/car/<car-id>/details/ - car details page
# •	http://localhost:8000/car/<car-id>/edit/ - car edit page
# •	http://localhost:8000/car/<car-id>/delete/ - car delete page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/ - profile delete page

urlpatterns = [
    path('', index, name='index_page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile_create'),
        path('details/', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car_create'),
        path('<int:pk>/details/', car_details, name='car_details'),
        path('<int:pk>/edit/', car_edit, name='car_edit'),
        path('<int:pk>/delete/', car_delete, name='car_delete'),
    ])), ]
