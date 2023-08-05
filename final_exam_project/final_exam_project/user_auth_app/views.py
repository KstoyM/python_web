from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from .forms import RegisterUserForm, EditUserForm


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
    form = AuthenticationForm
    success_url = reverse_lazy('index_page')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index_page')


class DetailsProfileView(views.DetailView):
    template_name = 'details_profile.html'
    model = get_user_model()


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
            'age': form.fields['age'],
            'profile_picture': form.fields['profile_picture'],
        }
        return form


class ProfileDeleteView(views.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('index_page')


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    form = auth_views.PasswordChangeForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        result = super().form_valid(form)

        return result
