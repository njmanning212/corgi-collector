from django.shortcuts import render 

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def corgis_index(request):
  return render(request, 'corgis/index.html', { 'corgis': corgis })