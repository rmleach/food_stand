from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='distros-home'),
    path('detail/', views.detail, name='distros-detail'),
]