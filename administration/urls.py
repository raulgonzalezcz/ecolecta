from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.show_catalogo, name='catalogo'),
    path('lugar_domestico/', views.show_lugar_domestico, name='lugar_domestico'),
    path('lugar_comercio/', views.show_lugar_comercio, name='lugar_comercio'),
    path('ruta/', views.show_ruta, name='rutas'),
    path('tesoreria/', views.show_tesoreria, name='tesoreria'),
]