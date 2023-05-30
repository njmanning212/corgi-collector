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
]