from django.urls import path
from . import views

# urlpatterns 
urlpatterns = [
    path('', views.home, name='home'),
    path('user_home/', views.user_home, name='user_home'),

    # accounts
    path('acc_details/', views.acc_details, name='acc_details'),
]