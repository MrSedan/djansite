from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.idenx, name='index'),   
]