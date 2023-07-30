from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserGroupInline(admin.TabularInline):
    model = UserModel.groups.through
    extra = 1

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'groups']
    inlines = (UserGroupInline,)


