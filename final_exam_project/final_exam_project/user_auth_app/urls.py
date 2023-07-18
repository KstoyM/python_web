from django.urls import path, include

from .views import RegisterUserView, LoginUserView, LogoutUserView, details_profile, edit_profile, delete_profile

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details_profile'),
        path('edit/', edit_profile, name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile')
    ])),
]
