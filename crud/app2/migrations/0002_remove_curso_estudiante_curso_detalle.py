# Generated by Django 5.1.4 on 2025-01-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='curso',
            name='detalle',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]