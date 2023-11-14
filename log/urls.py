from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_logs, name="logs"),
    path('view/<int:pk>/', views.view_log, name="view_log"),
    path('view/search/', views.log_search, name='log_search'),
]