from django.urls import path
from . import views

urlpatterns = [
    path('unidades', views.unidades, name="unidades"),
    path('unidades/buscar', views.buscar_unidade, name="buscar_unidade"),
    path('unidades/criar', views.criar_unidade, name="criar_unidade"),
    path('unidades/<int:pk>', views.editar_unidade, name="editar_unidade"),
    path('unidades/search/', views.unidades_search, name='unidades_search'),
]
