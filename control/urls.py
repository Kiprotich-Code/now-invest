from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

    # users 
    path('ctrl_users/', views.ctrl_users, name='ctrl_users'),
    path('add_user/', views.add_user, name='add_user'),
]