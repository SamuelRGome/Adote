from django.urls import path
from . import views

urlpatterns = [
    path('', views.peludos, name='peludos'),
    path('instagram', views.out, name='output')
]
