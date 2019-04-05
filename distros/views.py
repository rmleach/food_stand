from django.shortcuts import render
from .models import Post

distroSites = [
  {
  'site': 'Church of Rufus',
  'address': '123 Elm St',
  'info': 'COR Info',
  'last_updated': '11 Mar 2019'
  },
  {
  'site': 'Food Not Bombs Denver',
  'address': '123 14th Ave',
  'info': 'FNB Info',
  'last_updated': '13 Mar 2019'
  }
]

def home(request):
  context = {
    'distroSites': Post.objects.all()
  }
  return render(request, 'distros/home.html', context)

def detail(request):
  return render(request, 'distros/detail.html', {'site': 'detail'})
