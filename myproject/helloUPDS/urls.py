from django.urls import path
from helloUPDS import views

urlpatterns = [ 
 path('', views.helloUPDS, name='helloUPDS'),
]
