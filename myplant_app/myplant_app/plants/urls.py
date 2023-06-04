from .views import index, create, catalogue
from django.urls import path

urlpatterns = [
    path("", index, name='home-page'),
    path("create/", create, name='create-plant'),
    path("catalogue/", catalogue, name='catalogue-page')

]

#  plant pages

urlpatterns += [
    path("details/<plant_id>/", name='plant-details'),
    path("edit/<plant_id>/", name='edit-plant'),
    path("delete/<plant_id>/", name='delete-plant')
]

