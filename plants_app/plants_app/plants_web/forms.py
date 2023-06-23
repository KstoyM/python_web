from django import forms

from plants_app.plants_web.models import ProfileModel, PlantModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"


class ProfileForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = "__all__"


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
