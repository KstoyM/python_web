from django.contrib import admin
from .models import Car
# Register your models here.


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['make','model', 'currently_rented', 'created_at', 'modified_at']
    list_filter = ['currently_rented', 'created_at', 'modified_at']