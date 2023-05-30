from django.shortcuts import render 
from .models import Corgi

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def corgis_index(request):
  corgis = Corgi.objects.all()
  return render(request, 'corgis/index.html', { 'corgis': corgis })