# Generated by Django 3.0.2 on 2020-03-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0002_auto_20200302_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=50, null=True),
        ),
    ]
