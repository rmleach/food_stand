from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'distros/home.html')

def detail(request):
  return render(request, 'distros/detail.html')
