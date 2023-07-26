from django.urls import path, include

from .views import RegisterUserView, LoginUserView, LogoutUserView, DetailsProfileView, ProfileEditView, \
    ProfileDeleteView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('profile/<int:pk>/', include([
        path('', DetailsProfileView.as_view(), name='details_profile'),
        path('edit/', ProfileEditView.as_view(), name='edit_profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete_profile')
    ])),
]
