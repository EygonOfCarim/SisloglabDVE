from django.urls import path
from . import views

urlpatterns = [
    path('controle', views.controles, name="controles"),
    path('controle/criar', views.criar_controle, name="criar_controle"),
    path('controle/exportar', views.exportar_controles, name="exportar_controle"),
    path('controle/<int:ano>/<int:mes>', views.ver_controle, name="ver_controle"),
    path('controle/<int:pk>', views.editar_controle, name="editar_controle"),
    path('controle/deletar/<int:pk>', views.deletar_controle, name="deletar_controle"),
    path('controle/search/', views.controle_search, name='controle_search'),
    path('controle/search_export/', views.controle_export, name='controle_export'),
]
