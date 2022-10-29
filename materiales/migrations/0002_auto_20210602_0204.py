# Generated by Django 3.2.3 on 2021-06-02 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='material',
            name='nombre',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='materiales.tipomaterial',
                verbose_name='Nombre'),
        ),
    ]