from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

UserModel = get_user_model()


class UserGroupInline(admin.TabularInline):
    model = UserModel.groups.through
    extra = 1


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['date_joined', 'username', 'email','first_name', 'last_name', 'age']
    list_filter = ['groups']
    inlines = (UserGroupInline,)
    exclude = ('groups', 'superuser_status', 'user_permissions','is_staff')


class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_users']

    def display_users(self, obj):
        users = obj.user_set.all()
        if users:
            user_links = [
                format_html(
                    '<a href="{}">{}</a>',
                    reverse('admin:%s_%s_change' % (user._meta.app_label, user._meta.model_name), args=[user.id]),
                    user.username
                )
                for user in users
            ]
            return format_html('<br>'.join(user_links))
        return None

    display_users.short_description = 'Users'


# Unregister the default GroupAdmin
admin.site.unregister(Group)

# Register the CustomGroupAdmin for the Group model
admin.site.register(Group, CustomGroupAdmin)
