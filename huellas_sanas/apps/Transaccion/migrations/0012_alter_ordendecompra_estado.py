# Generated by Django 4.2.5 on 2023-11-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaccion', '0011_alter_ordendecompra_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='estado',
            field=models.CharField(default='pendiente', max_length=20),
        ),
    ]
