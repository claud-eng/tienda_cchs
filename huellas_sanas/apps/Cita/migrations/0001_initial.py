# Generated by Django 4.2.5 on 2023-09-20 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('historial_medico', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('motivo', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('Mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cita.mascota')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.cliente')),
                ('veterinario', models.ForeignKey(limit_choices_to={'user__is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to='Usuario.empleado')),
            ],
        ),
    ]
