from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroAspiranteForm
from .models import Aspirante, FormacionAcademica, InformacionAdicional, Residencia, Participacion, Documentos, RolAspirante

def form_view(request):
    if request.method == 'POST':
        form = RegistroAspiranteForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar la información del aspirante
            aspirante = Aspirante.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido_paterno=form.cleaned_data['apellido_paterno'],
                apellido_materno=form.cleaned_data['apellido_materno'],
                correo=form.cleaned_data['correo'],
                telefono=form.cleaned_data['telefono']
            )

            # Crear Formacion Académica
            FormacionAcademica.objects.create(
                aspirante=aspirante,
                nivel_academico=form.cleaned_data['nivel_academico'],
                certificado_constancia=form.cleaned_data['certificado_constancia']
            )

            # Crear Información Adicional
            InformacionAdicional.objects.create(
                aspirante=aspirante,
                habla_lengua_indigena=form.cleaned_data['habla_lengua_indigena'] == 'sí',
                talla_playera=form.cleaned_data['talla_playera'],
                talla_pantalon=form.cleaned_data['talla_pantalon'],
                talla_calzado=form.cleaned_data['talla_calzado'],
                banco=form.cleaned_data['banco'],
                cuenta_bancaria=form.cleaned_data['cuenta_bancaria']
            )

            # Crear Residencia
            Residencia.objects.create(
                aspirante=aspirante,
                codigo_postal=form.cleaned_data['codigo_postal'],
                estado=form.cleaned_data['estado'],
                municipio=form.cleaned_data['municipio'],
                localidad=form.cleaned_data['localidad'],
                colonia=form.cleaned_data['colonia']
            )

            # Crear Participación
            Participacion.objects.create(
                aspirante=aspirante,
                estado_participacion=form.cleaned_data['estado_participacion'],
                ciclo_escolar=form.cleaned_data['ciclo_escolar']
            )

            # Crear Documentos
            Documentos.objects.create(
                aspirante=aspirante,
                identificacion_oficial=form.cleaned_data['identificacion_oficial'],
                fotografia=form.cleaned_data['fotografia'],
                comprobante_domicilio=form.cleaned_data['comprobante_domicilio']
            )

            # Crear Rol Aspirante
            RolAspirante.objects.create(
                aspirante=aspirante,
                rol_aplica=form.cleaned_data['rol_aplica']
            )

            # Mensaje de éxito
            messages.success(request, 'Aspirante subido al sistema exitosamente.')

            # Redirigir a una página de éxito o al mismo formulario
            return redirect('app_form/mensaje.html')  # Cambia 'nombre_de_la_vista_de_confirmacion' al nombre de tu vista de confirmación o la URL donde quieras redirigir.
    else:
        form = RegistroAspiranteForm()

    return render(request, 'app_form/template_form.html', {'form': form})  # Cambia 'nombre_de_tu_template.html' por el nombre de tu template

def confirmacion(request):
    return render(request, 'confirmacion.html')


