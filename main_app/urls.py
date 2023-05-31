from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('corgis/', views.corgis_index, name='corgi-index'),
  path('corgis/<int:corgi_id>/', views.corgis_detail, name='corgi-detail'),
  path('corgis/create/', views.CorgiCreate.as_view(), name='corgi-create'),
  path('corgis/<int:pk>/update/', views.CorgiUpdate.as_view(), name='corgi-update'),
  path('corgis/<int:pk>/delete/', views.CorgiDelete.as_view(), name='corgi-delete'),
  path('corgis/<int:corgi_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('corgis/<int:corgi_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
]