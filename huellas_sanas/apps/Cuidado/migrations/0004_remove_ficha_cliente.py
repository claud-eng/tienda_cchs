# Generated by Django 4.2.5 on 2023-10-02 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuidado', '0003_ficha_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='cliente',
        ),
    ]
