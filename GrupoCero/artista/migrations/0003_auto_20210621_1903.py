# Generated by Django 3.2.4 on 2021-06-21 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0002_auto_20210621_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editarperfil',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfil'},
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='alto',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')], verbose_name='Alto'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='ancho',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')], verbose_name='Ancho'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='anio',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')], verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='precio',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^\\d{1,9}$')], verbose_name='Precio ($CLP)'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='soporte',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Soporte'),
        ),
    ]
