from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


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
  ordering = ['-last_updated']

class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['address', 'info']

  def form_valid(self, form):
    form.instance.site = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['address', 'info']

  def form_valid(self, form):
    form.instance.site = self.request.user
    return super().form_valid(form)


def detail(request):
  return render(request, 'distros/detail.html', {'site': 'detail'})
