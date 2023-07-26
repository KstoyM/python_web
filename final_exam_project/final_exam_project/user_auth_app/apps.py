from django.apps import AppConfig


class UserAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'final_exam_project.user_auth_app'

    def ready(self):
        result = super().ready()
        from . import signals
        return result
