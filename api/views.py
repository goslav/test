from rest_framework import viewsets

from .serializers import CitizenSerializer
from citizens.models import Citizen


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all().order_by('id_number')
    serializer_class = CitizenSerializer
