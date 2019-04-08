from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def home(request):
  context = {
    'distroSites': Post.objects.all()
  }
  mapbox_access_token = 'pk.eyJ1IjoibGVhY2hpc2FuIiwiYSI6ImNqdTRlZzF6bzB4NGc0M3Bkd3FwZ3QwNG4ifQ.ifl_XV7nHgm1qpoaMp2uKw'
  return render(request, 'distros/home.html', context,{'mapbox_access_token': mapbox_access_token})

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


def detail(request):
  return render(request, 'distros/detail.html', {'site': 'detail'})
