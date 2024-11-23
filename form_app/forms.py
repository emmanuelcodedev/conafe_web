from django import forms

class RegistroAspiranteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    nivel_academico = forms.ChoiceField(choices=[('1', 'Primaria'), ('2', 'Secundaria'), ('3', 'Preparatoria')])
    titulo_obtenido = forms.CharField(max_length=255)
    institucion = forms.CharField(max_length=255)
    rol_aplica = forms.CharField(max_length=100)
    certificado = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Asignación de clases a los campos
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellidos'].widget.attrs.update({'class': 'form-control'})
        self.fields['correo'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['nivel_academico'].widget.attrs.update({'class': 'form-control'})
        self.fields['titulo_obtenido'].widget.attrs.update({'class': 'form-control'})
        self.fields['institucion'].widget.attrs.update({'class': 'form-control'})
        self.fields['rol_aplica'].widget.attrs.update({'class': 'form-control'})
        self.fields['certificado'].widget.attrs.update({'class': 'form-control'})

