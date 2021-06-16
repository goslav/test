from django.contrib import admin
from .models import Citizen


class CitizenAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'date_of_birth')


admin.site.register(Citizen, CitizenAdmin)
