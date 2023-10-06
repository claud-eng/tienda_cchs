# Generated by Django 4.2.5 on 2023-10-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0012_alter_cliente_fecha_nacimiento_and_more'),
        ('Cuidado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='veterinario',
            field=models.ForeignKey(limit_choices_to={'rol': 'Veterinario'}, on_delete=django.db.models.deletion.CASCADE, to='Usuario.empleado'),
        ),
    ]
