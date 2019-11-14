from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'), 
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('id/<str:s>/', views.profile, name='profile'),
]