# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matrimonio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('apellido_matrimonio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_persona', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]
