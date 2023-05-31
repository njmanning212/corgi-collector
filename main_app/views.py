from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Corgi
from .forms import FeedingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def corgis_index(request):
  corgis = Corgi.objects.all()
  return render(request, 'corgis/index.html', { 'corgis': corgis })

def corgis_detail(request, corgi_id):
  corgi = Corgi.objects.get(id=corgi_id)
  feeding_form = FeedingForm()
  return render(request, 'corgis/detail.html', { 
    'corgi': corgi,
    'feeding_form': feeding_form 
  })

class CorgiCreate(CreateView):
  model = Corgi
  fields = ['name', 'type', 'description', 'age']

class CorgiUpdate(UpdateView):
  model = Corgi
  fields = ['type', 'description', 'age']

class CorgiDelete(DeleteView):
  model = Corgi
  success_url = '/corgis/'

def add_feeding(request, corgi_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.corgi_id = corgi_id
    new_feeding.save()
  return redirect('corgi-detail', corgi_id=corgi_id)