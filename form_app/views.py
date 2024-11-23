from django.shortcuts import render
from .forms import RegistroAspiranteForm

def form_view(request):
    if request.method == 'POST':
        form = RegistroAspiranteForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar los datos y guardar en la base de datos o realizar otras acciones
            return render(request, 'confirmation.html', {'form': form})
    else:
        form = RegistroAspiranteForm()
    return render(request, 'app_form/template_form.html', {'form': form})
