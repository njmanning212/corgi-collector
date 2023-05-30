from django.shortcuts import render 

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Corgi

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def corgis_index(request):
  corgis = Corgi.objects.all()
  return render(request, 'corgis/index.html', { 'corgis': corgis })

def corgis_detail(request, corgi_id):
  corgi = Corgi.objects.get(id=corgi_id)
  return render(request, 'corgis/detail.html', { 'corgi': corgi })

class CorgiCreate(CreateView):
  model = Corgi
  fields = ['name', 'type', 'description', 'age']

class CorgiUpdate(UpdateView):
  model = Corgi
  fields = ['type', 'description', 'age']

class CorgiDelete(DeleteView):
  model = Corgi
  success_url = '/corgis/'