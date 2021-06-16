from django.urls import path
from .import views

app_name = 'citizens'

urlpatterns = [
    path('', views.indexPage, name="index"),
]
