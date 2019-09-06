from django.urls import path

from . import views

app_name = 'ecolector'
urlpatterns = [
    path('reporte/', views.show_reportes, name='reportes'),
    path('saldo/', views.show_saldo, name='saldo'),
    path('ruta-disponible/', views.show_rutas_disponibles, name='rutas_disponibles'),
    path('ruta-completada/', views.show_rutas_completadas, name='rutas_completadas'),
]