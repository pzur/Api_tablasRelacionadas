# Generated by Django 3.0.2 on 2020-03-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0003_auto_20200302_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='tipo_animal',
        ),
        migrations.AddField(
            model_name='mascota',
            name='tipo_mascota',
            field=models.CharField(blank=True, choices=[('Perro', 'Perro'), ('Gato', 'Gato')], max_length=50, null=True),
        ),
    ]