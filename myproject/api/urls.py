from django.urls import path
from api import views

urlpatterns = [ 
    path('', views.mostrar_api, name='api'),
]