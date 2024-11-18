from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from login_app.decorators import role_required
from .forms import EmpleadoForm
from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import UsuarioRol  
from .models import Empleado

@login_required
@role_required('DOT')
def dashboard_view(request):
    return render(request, 'home_dot/dot_home.html')


@login_required
@role_required('DOT')
def agregar_trabajador(request):
    """
    Vista para agregar un nuevo trabajador, solo accesible por el rol 'DOT'.
    """
    edades = range(18, 66)  # Rango de edades entre 18 y 65

    if request.method == 'POST':
        # Si el formulario es enviado con POST
        form = EmpleadoForm(request.POST, request.FILES)  # Suponiendo que tienes un formulario
        if form.is_valid():
            # Procesar los datos del formulario para guardar el usuario y el empleado
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            edad = form.cleaned_data['edad']
            genero = form.cleaned_data['genero']
            salario = form.cleaned_data['salario']
            foto = form.cleaned_data['foto']
            rol = form.cleaned_data['rol']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Crear el usuario
            usuario = UsuarioRol.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=nombre,
                last_name=apellido,
                role=rol
            )

            # Crear el empleado
            empleado = Empleado.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                edad=edad,
                genero=genero,
                salario=salario,
                foto=foto,
                rol=rol,
                usuario=usuario
            )

            # Agregar un mensaje de éxito
            messages.success(request, '¡Trabajador agregado exitosamente!')
            return redirect('dot_home:home_dot')  # Redirige a la vista 'home_dot' (dashboard principal)
    else:
        form = EmpleadoForm()  # Si es GET, solo se muestra el formulario vacío
    
    return render(request, 'home_dot/home_agregar.html', {'edades': edades, 'form': form})
