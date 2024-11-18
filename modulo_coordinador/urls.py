from django.urls import path
from . import views
app_name = 'coordinador_home'
urlpatterns = [
    path('home_coordinador/', views.empleado_view, name='home_coordinador'),  # Define la vista de home_empleado
]



