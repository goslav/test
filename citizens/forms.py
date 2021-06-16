from django import forms
from .models import Citizen
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import DateInput


class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = '__all__'
        labels = {
            'id_number': _('ID'),
            'date_of_birth': _('DATE OF BIRTH'),
        }
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }
