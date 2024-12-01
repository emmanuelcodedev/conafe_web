from django import forms
from .models import Aspirante
from .models import validate_phone_number  # Suponiendo que hayas definido este validador

# Lista de estados mexicanos como constante fuera de la clase
ESTADOS_MEXICO = [
    ('aguascalientes', 'Aguascalientes'),
    ('baja_california', 'Baja California'),
    ('baja_california_sur', 'Baja California Sur'),
    ('campeche', 'Campeche'),
    ('chiapas', 'Chiapas'),
    ('chihuahua', 'Chihuahua'),
    ('ciudad_de_mexico', 'Ciudad de México'),
    ('coahuila', 'Coahuila'),
    ('colima', 'Colima'),
    ('durango', 'Durango'),
    ('guanajuato', 'Guanajuato'),
    ('guerrero', 'Guerrero'),
    ('hidalgo', 'Hidalgo'),
    ('jalisco', 'Jalisco'),
    ('edo_mexico', 'Estado de México'),
    ('michoacan', 'Michoacán'),
    ('morelos', 'Morelos'),
    ('nayarit', 'Nayarit'),
    ('nuevo_leon', 'Nuevo León'),
    ('oaxaca', 'Oaxaca'),
    ('puebla', 'Puebla'),
    ('queretaro', 'Querétaro'),
    ('quintana_roo', 'Quintana Roo'),
    ('san_luis_potosi', 'San Luis Potosí'),
    ('sinaloa', 'Sinaloa'),
    ('sonora', 'Sonora'),
    ('tabasco', 'Tabasco'),
    ('tamaulipas', 'Tamaulipas'),
    ('tlaxcala', 'Tlaxcala'),
    ('veracruz', 'Veracruz'),
    ('yucatan', 'Yucatán'),
    ('zacatecas', 'Zacatecas'),
]

# Form principal
class RegistroAspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'telefono']
    
    telefono = forms.CharField(
        max_length=15,
        label="Número de Teléfono",
        validators=[validate_phone_number]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})
            elif isinstance(field.widget, forms.widgets.RadioSelect):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


"""
    # Formación Académica
    nivel_academico = forms.ChoiceField(
        choices=[
            ('1', 'Primaria'),
            ('2', 'Secundaria'),
            ('3', 'Preparatoria'),
            ('4', 'Universidad'),
            ('5', 'Maestría'),
            ('6', 'Doctorado')
        ],
        label="Nivel Académico"
    )
    habla_lengua_indigena = forms.ChoiceField(
        choices=[('sí', 'Sí'), ('no', 'No')],
        label="¿Hablas alguna lengua indígena?",
        widget=forms.RadioSelect()
    )
    certificado_constancia = forms.FileField(label="Certificado del último grado de estudios")

    # Información Adicional
    talla_playera = forms.ChoiceField(
        choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')],
        label="Talla de Playera"
    )
    talla_pantalon = forms.CharField(max_length=10, label="Talla de Pantalón")
    talla_calzado = forms.CharField(max_length=10, label="Talla de Calzado")
    banco = forms.CharField(max_length=100, label="Banco")
    cuenta_bancaria = forms.CharField(max_length=50, label="Cuenta Bancaria")

    # Residencia
    codigo_postal = forms.CharField(max_length=15, label="Código Postal")
    estado = forms.ChoiceField(
        choices=ESTADOS_MEXICO,
        label="Estado",
    )
    municipio = forms.CharField(max_length=100, label="Municipio o Alcaldía")
    localidad = forms.CharField(max_length=100, label="Localidad")
    colonia = forms.CharField(max_length=100, label="Colonia")

    # Participación
    estado_participacion = forms.ChoiceField(
        choices=ESTADOS_MEXICO,
        label="Estado en el que deseas participar"
    )
    ciclo_escolar = forms.CharField(max_length=100, label="Ciclo Escolar a participar")

    # Documentos
    identificacion_oficial = forms.FileField(label="Identificación oficial")
    fotografia = forms.FileField(label="Fotografía reciente")
    comprobante_domicilio = forms.FileField(label="Comprobante de domicilio")

    # Rol al que aplica
    rol_aplica = forms.ChoiceField(
        choices=[
            ('maestro', 'Maestro'),
            ('administrador', 'Administrador'),
            ('asistente', 'Asistente'),
            ('educador_comunitario', 'Educador Comunitario (EC)')
        ],
        label="Rol al que Aplica",
        initial='educador_comunitario',
        widget=forms.HiddenInput()  # Campo oculto
    )
"""




