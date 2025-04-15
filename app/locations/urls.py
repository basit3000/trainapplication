from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('', views.list, name='list'),
    path('add', views.add_location, name='add'),
]