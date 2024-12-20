# Generated by Django 4.2.4 on 2024-12-01 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0006_residencia_participacion_informacionadicional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionadicional',
            name='banco',
            field=models.CharField(choices=[('BBVA', 'BBVA'), ('Santander', 'Santander'), ('Banorte', 'Banorte'), ('HSBC', 'HSBC'), ('Citibanamex', 'Citibanamex'), ('Scotiabank', 'Scotiabank'), ('Inbursa', 'Inbursa'), ('Bajío', 'Bajío'), ('Monex', 'Monex'), ('BancoAzteca', 'Banco Azteca'), ('Banregio', 'Banregio'), ('Compartamos', 'Compartamos'), ('Otros', 'Otros')], max_length=150),
        ),
        migrations.AlterField(
            model_name='informacionadicional',
            name='talla_calzado',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
