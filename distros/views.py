from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
import json


def home(request):
  context = {
    'distroSites': Post.objects.all()
  }
  google_access_token = 'AIzaSyBI7H13xNvaarHZgcRU0akjiHnd_saxE_Y'
  return render(request, 'distros/home.html', context,{'google_access_token': google_access_token})

class PostListView(ListView):
  model = Post
  template_name = 'distros/home.html'
  context_object_name = 'distroSites'
  ordering = ['-start_time']

class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['address', 'info']

  def form_valid(self, form):
    form.instance.site = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['address', 'info']

  def form_valid(self, form):
    form.instance.site = str(self.request.user)
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.site:
      return True
    return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.site:
      return True
    return False

def detail(request):
  return render(request, 'distros/detail.html', {'site': 'detail'})
