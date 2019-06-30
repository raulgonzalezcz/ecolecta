from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.index, name='index'),
    path('lugar/', views.show_lugar, name='lugar'),
    path('ruta/', views.show_ruta, name='rutas'),
]