from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from final_exam_project import settings

UserModel = get_user_model()


def send_successful_registration_email(user):

    send_mail(
        subject='Successful registration',
        message=f'Hello {user.username},\n\n'
                f'You have successfully registered in our website.\n\n'
                f'Best regards,\n'
                f'Rent-a-car team',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
