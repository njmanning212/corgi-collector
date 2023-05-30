from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('corgis/', views.corgis_index, name='cargi-index'),
  path('corgis/<int:corgi_id>/', views.corgis_detail, name='corgi-detail'),
]