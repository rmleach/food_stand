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
  mapbox_access_token = 'pk.eyJ1IjoibGVhY2hpc2FuIiwiYSI6ImNqdTRlZzF6bzB4NGc0M3Bkd3FwZ3QwNG4ifQ.ifl_XV7nHgm1qpoaMp2uKw'
  return render(request, 'distros/home.html', context,{'mapbox_access_token': mapbox_access_token})




def detail(request):
  return render(request, 'distros/detail.html', {'site': 'detail'})
