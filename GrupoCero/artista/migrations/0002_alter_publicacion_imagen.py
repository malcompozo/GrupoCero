# Generated by Django 3.2.4 on 2021-07-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='obras', verbose_name='Imagen'),
        ),
    ]
