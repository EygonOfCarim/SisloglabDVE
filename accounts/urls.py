from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name="users"),
    path('users/create', views.user_create, name="user_create"),
    path('users/edit<str:pk>', views.user_edit, name="user_edit"),
    path('users/search/', views.users_search, name='users_search'),
]
