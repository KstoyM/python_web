from .views import index, details, details_template,details_error
from django.urls import path

urlpatterns = [
    path("", index),
    path("/<int:department_id>/", details, name='departments int'),
    path("template/<int:department_id>/", details_template),
    path("template/<int:department_id>/", details_error),
    path("<department_id>/", details)
]