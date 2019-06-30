from django.urls import path

from . import views

app_name = 'ecolector'
urlpatterns = [
    path('', views.index, name='index'),
    path('saldo/', views.show_saldo, name='saldo'),
    path('ruta/', views.show_rutas, name='rutas'),
]