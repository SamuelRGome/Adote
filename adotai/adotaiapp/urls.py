from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('central/',views.central, name='central'),
    path('peludos/', views.peludos, name='peludos'),
    path('instagram', views.out, name='output')
]
