from django.contrib import admin
from .models import Signing


class SigningAdmin(admin.ModelAdmin):
    list_display = ('user', 'clock_in_time', 'clock_out_time', 'has_clocked_out', 'date')

admin.site.register(Signing, SigningAdmin)
