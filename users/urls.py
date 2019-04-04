from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('detail/', views.detail, name='users-detail'),
]
