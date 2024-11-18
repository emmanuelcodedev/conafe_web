# urls.py
from django.urls import path
from . import views

app_name = 'dot_home'

urlpatterns = [
    # Ruta para el dashboard principal
    path('home_dot/', views.dashboard_view, name='home_dot'),

    # Ruta para agregar trabajador
    path('agregar_usuario/', views.agregar_trabajador, name='home_agregar'),

    # Ruta para una vista de confirmación después de agregar un trabajador (si es necesario)
    path('dashboard_agregar/', views.dashboard_view, name='dashboard_agregar'),
]




