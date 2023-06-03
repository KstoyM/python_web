from .views import index, create, catalogue
from django.urls import path

urlpatterns = [
    path("", index, name='home-page'),
    path("create/", create, name='plant-create-page'),  # plant create page
    path("catalogue/", catalogue, name='catalogue-page')

]

#  plant pages

urlpatterns += [
    path("details/<plant_id>/", name='plant-details-page'),
    path("edit/<plant_id>/", name='plant-edit-page'),
    path("delete/<plant_id>/", name='plant-delete-page')
]

