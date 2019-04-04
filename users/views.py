from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>User List</h1>')

def detail(request):
  return HttpResponse('<h1>User Detail View</h1>')
