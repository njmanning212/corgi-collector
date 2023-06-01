from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Corgi, Toy
from .forms import FeedingForm

class Home(LoginView):
  template_name = 'home.html'

@login_required
def about(request):
  return render(request, 'about.html')

@login_required

def corgis_index(request):
  corgis = Corgi.objects.filter(user=request.user)
  return render(request, 'corgis/index.html', { 'corgis': corgis })

@login_required
def corgis_detail(request, corgi_id):
  corgi = Corgi.objects.get(id=corgi_id)
  feeding_form = FeedingForm()
  toys_corgi_doesnt_have = Toy.objects.exclude(id__in = corgi.toys.all().values_list('id'))
  return render(request, 'corgis/detail.html', { 
    'corgi': corgi,
    'feeding_form': feeding_form, 
    'toys': toys_corgi_doesnt_have 
  })

class CorgiCreate(LoginRequiredMixin, CreateView):
  model = Corgi
  fields = ['name', 'type', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CorgiUpdate(LoginRequiredMixin, UpdateView):
  model = Corgi
  fields = ['type', 'description', 'age']

class CorgiDelete(DeleteView):
  model = Corgi
  success_url = '/corgis/'

@login_required
def add_feeding(request, corgi_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.corgi_id = corgi_id
    new_feeding.save()
  return redirect('corgi-detail', corgi_id=corgi_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

@login_required
def assoc_toy(request, corgi_id, toy_id):
  Corgi.objects.get(id=corgi_id).toys.add(toy_id)
  return redirect('corgi-detail', corgi_id=corgi_id)

@login_required
def unassoc_toy(request, corgi_id, toy_id):
  Corgi.objects.get(id=corgi_id).toys.remove(toy_id)
  return redirect('corgi-detail', corgi_id=corgi_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('corgi-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'signup.html', context)