# Generated by Django 3.2.13 on 2022-10-13 17:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0008_tipooperacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipooperacion',
            options={'ordering': ['nombre_tipo', '-precio_unitario'], 'verbose_name': 'TipoDeOperacion', 'verbose_name_plural': 'TiposDeOperaciones'},
        ),
        migrations.RemoveField(
            model_name='operacion',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='operacion',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='tipooperacion',
            name='nombre',
        ),
        migrations.AddField(
            model_name='operacion',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio Total'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operaciones.tipooperacion'),
        ),
        migrations.AddField(
            model_name='tipooperacion',
            name='nombre_tipo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Operación'),
        ),
        migrations.AlterModelTable(
            name='tipooperacion',
            table='tipo_oper',
        ),
    ]
