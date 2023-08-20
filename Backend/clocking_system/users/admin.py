from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'salary', 'time_worked_this_month', 'salary_so_far_this_month', )

admin.site.register(CustomUser, CustomUserAdmin)
