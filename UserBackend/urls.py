from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('get_user/', views.get_user),
    path('get_cart/', views.get_cart),
    path('post_cart/', views.post_cart),
    path('delete_cart/', views.delete_cart),
    path('change/', views.change),
    path('register/', views.register)
]