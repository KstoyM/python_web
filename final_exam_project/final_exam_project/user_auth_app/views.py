from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from .forms import RegisterUserForm, LoginUserForm



# Create your views here.
# path('login/', login_user, name='login user'),
# path('logout/', logout_user, name='logout user'),
# path('register/', register_user, name='register user'),
# path('profile/', include([
#     path('details/', details_profile, name='details profile'),
#     path('edit/', edit_profile, name='edit profile'),
#     path('delete/', delete_profile, name='delete profile')
# ])),

# class OnlyAnonymousMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponse(self.get_success_url())
#
#         return super().dispatch(request, *args, **kwargs)


class RegisterUserView(views.CreateView):
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['next'] = self.request.GET.get('next', '')
    #
    #     return context
    #
    # def get_success_url(self):
    #
    #     return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'login_page.html'
    form = LoginUserForm
    success_url = reverse_lazy('index_page')



class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index_page')


def details_profile(request, pk):
    user_profile = get_user_model().objects.get(pk=pk)
    return render(request, 'details_profile.html', {'user_profile': user_profile})


def edit_profile(request):
    return render(request, 'edit_profile.html')


def delete_profile(request):
    return render(request, 'delete_profile.html')
