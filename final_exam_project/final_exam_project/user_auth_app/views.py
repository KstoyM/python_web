from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from .forms import RegisterUserForm, LoginUserForm, EditUserForm


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


class LoginUserView(auth_views.LoginView):
    template_name = 'login_page.html'
    form = LoginUserForm
    success_url = reverse_lazy('index_page')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index_page')


# def details_profile(request, pk):
#     user_profile = get_user_model().objects.get(pk=pk)
#     return render(request, 'details_profile.html', {'user_profile': user_profile})


class DetailsProfileView(views.DetailView):
    template_name = 'details_profile.html'
    model = get_user_model()

    # def get_context_data(self, **kwargs):
    #     profile_image = static('images/profile_image.jpg')
    #
    #     if self.object.profile_picture is not None:
    #         profile_image = self.object.profile_image
    #
    #     context = super().get_context_data(**kwargs)
    #     context['profile_image'] = profile_image
    #     return context


class ProfileEditView(views.UpdateView):
    template_name = 'edit_profile.html'
    form_class = EditUserForm
    model = get_user_model()

    def get_success_url(self):
        # Redirect to 'details_profile' URL with the updated user's pk
        return reverse('details_profile', kwargs={'pk': self.kwargs['pk']})

    def get_form(self, form_class=None):
        # Use the form specified in form_class attribute
        form = super().get_form(form_class=self.form_class)
        # Specify the fields you want to include in the form
        form.fields = {
            'username': form.fields['username'],
            'email': form.fields['email'],
            'first_name': form.fields['first_name'],
            'last_name': form.fields['last_name'],
            'profile_picture': form.fields['profile_picture'],
        }
        return form


class ProfileDeleteView(views.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('index_page')
