from django.db import models
from django.core.exceptions import ValidationError
import re
from django import forms

# Función para validar el tamaño del archivo
def validate_file_size(file):
    max_size = 5 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError("El archivo es demasiado grande.")
    return file

def validate_phone_number(value):
    if not re.match(r'^\+?\d+$', value):  # Permitirá números con o sin el signo +
        raise ValidationError('El número de teléfono solo debe contener números y, opcionalmente, un signo + al inicio.')

class Aspirante(models.Model):
    # Información Personal
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15, validators=[validate_phone_number])

    def save(self, *args, **kwargs):
        # Asegura que solo se guarden números en el campo telefono
        self.telefono = ''.join(filter(str.isdigit, str(self.telefono)))  # Elimina caracteres no numéricos
        super(Aspirante, self).save(*args, **kwargs)

    class Meta:
        db_table = 'aspirante'  # Cambié la tabla a minúsculas

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    
"""
class FormacionAcademica(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='formaciones_academicas', on_delete=models.CASCADE)
    nivel_academico = models.CharField(max_length=150)
    titulo_obtenido = models.CharField(max_length=255)
    certificado_constancia = models.FileField(upload_to='documentos_academicos/', validators=[validate_file_size])

    class Meta:
        db_table = 'formacion_academica'

    def __str__(self):
        return f"{self.aspirante} - {self.nivel_academico}"
    

class InformacionAdicional(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='informaciones_adicionales', on_delete=models.CASCADE)
    habla_lengua_indigena = models.BooleanField(default=False)
    talla_playera = models.CharField(max_length=5)
    talla_pantalon = models.CharField(max_length=5)
    talla_calzado = models.PositiveIntegerField()
    banco = models.CharField(max_length=150)
    cuenta_bancaria = models.CharField(max_length=20)

    class Meta:
        db_table = 'informacion_adicional'

    def __str__(self):
        return f"{self.aspirante} - {self.talla_playera} - {self.banco}"

class Residencia(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='residencias', on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=10)
    estado = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)

    class Meta:
        db_table = 'residencia'

    def __str__(self):
        return f"{self.aspirante} - {self.estado} - {self.colonia}"

class Participacion(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='participaciones', on_delete=models.CASCADE)
    estado_participacion = models.CharField(max_length=100)
    ciclo_escolar = models.CharField(max_length=50)

    class Meta:
        db_table = 'participacion'

    def __str__(self):
        return f"{self.aspirante} - {self.estado_participacion} - {self.ciclo_escolar}"

class Documentos(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='documentos', on_delete=models.CASCADE)
    identificacion_oficial = models.FileField(upload_to='documentos_identificacion/', validators=[validate_file_size])
    fotografia = models.ImageField(upload_to='fotografias_aspirantes/')
    comprobante_domicilio = models.FileField(upload_to='documentos_domicilio/', validators=[validate_file_size])

    class Meta:
        db_table = 'documentos'

    def __str__(self):
        return f"{self.aspirante} - Documentos"

class RolAspirante(models.Model):
    aspirante = models.ForeignKey(Aspirante, related_name='roles', on_delete=models.CASCADE)
    rol_aplica = models.CharField(max_length=50)  # Ejemplo: 'Educador Comunitario'

    class Meta:
        db_table = 'rol_aspirante'

    def __str__(self):
        return f"{self.aspirante} - {self.rol_aplica}"
"""

