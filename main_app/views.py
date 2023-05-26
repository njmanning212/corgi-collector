from django.shortcuts import render

from django.http import HttpResponse

class Corgi:
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

corgis = [
  Corgi('Toffee', 'Pembroke Welsh', 'All about the foot', 4),
  Corgi('Bilbo', 'Pembroke Welsh', 'The best herder', 3),
  Corgi('Welshi', 'Cardigan Welsh', 'Short legs, big heart', 2),
  Corgi('Pancake', 'Pembroke Welsh', 'The new pup on the scene', 0),
]    

def home(request):
  return HttpResponse('<h1>Corgi Collector</h1>')


def about(request):
  return render(request, 'about.html')

def corgis_index(request):
  return render(request, 'corgis/index.html', { 'corgis': corgis })