from django.urls import path
from . import views

app_name = 'ex00'

urlpatterns = [
    path('', views.index, name='index'),
]