# Generated by Django 5.1.4 on 2025-01-03 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
        ('app2', '0002_remove_curso_estudiante_curso_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='direccion',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app2.curso'),
            preserve_default=False,
        ),
    ]
