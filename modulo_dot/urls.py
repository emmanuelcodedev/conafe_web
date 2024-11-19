# urls.py
from django.urls import path
from . import views

app_name = 'dot_home'

urlpatterns = [
    # Ruta para el dashboard principal
    path('home_dot/', views.home_view, name='home_dot'),
    
    # Ruta para agregar trabajador
    path('agregar_usuario/', views.agregar_trabajador, name='home_agregar'),
    
    # Ruta para visualizar dashboard
    path('visualizar_dashboard/', views.dashboard_view, name='dashboard_visualizar'),
    
    # Ruta para los detalles del empleado
    path('detalles_empleado/<int:empleado_id>/', views.detalles_empleado, name='detalles_empleado'),
]





