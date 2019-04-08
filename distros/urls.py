from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='distros-home'),
    path("<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("new/", PostCreateView.as_view(), name='post-create'),
    path('detail', views.detail, name='distros-detail'),
]
