from django.test import TestCase
from .models import Citizen
from . import views
from django.urls import resolve
import datetime


class CitizenTest(TestCase):

    def setUp(self):
        Citizen.objects.create(id_number="12345678",
                               date_of_birth="2021-01-01")
        Citizen.objects.create(id_number="87654321",
                               date_of_birth="2021-02-01")

    def test_citizen_was_born(self):
        citizen1 = Citizen.objects.get(id_number="12345678")
        citizen2 = Citizen.objects.get(id_number="87654321")
        self.assertEqual(citizen1.date_of_birth, datetime.date(2021, 1, 1))
        self.assertEqual(citizen2.date_of_birth, datetime.date(2021, 2, 1))


class indexPageTest(TestCase):

    def test_index_url(self):
        found = resolve('/')
        self.assertEqual(found.func, views.indexPage)
