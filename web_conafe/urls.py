from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Vista para redirigir a login
def redirect_to_login(request):
    return redirect('login')  # Redirige a la URL de login definida en 'login_app.urls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login),  # Redirige a la página de login cuando acceden a la raíz
    path('login/', include('login_app.urls')),  # Redirige a las URLs de login
    path('dot_section/', include(('modulo_dot.urls', 'dot_home'), namespace='dot_home')),
    path('empleado_section/', include(('home_empleado.urls', 'dashboard_empleado'), namespace='dashboard_empleado')),
    path('coordinador_section/', include(('modulo_coordinador.urls', 'coordinador_home'), namespace='coordinador_home')),
    
]



