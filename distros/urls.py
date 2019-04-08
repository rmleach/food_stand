from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='distros-home'),
    path("<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("new/", PostCreateView.as_view(), name='post-create'),
    path("<int:pk>/update", PostUpdateView.as_view(), name='post-update'),
    path('detail', views.detail, name='distros-detail'),
]
