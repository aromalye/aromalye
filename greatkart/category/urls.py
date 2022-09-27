from django.urls import path, include
from greatkart import views

urlpatterns = [
    path('', views.home, name='home'),
]