from django import forms

from games_app.games_web.models import GameModel, Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            "password": forms.PasswordInput(attrs={'data-toggle': 'password'}), }


class ProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = [
            'email',
            'age',
            'password',
        ]

class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class DeleteGameForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
