# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20180604_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento_Dinero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_movimiento', models.DateField()),
                ('tipo_movimiento', models.CharField(max_length=50)),
                ('clase_movimiento', models.CharField(max_length=10)),
                ('monto_movimiento', models.CharField(max_length=10)),
                ('descripcion_movimiento', models.CharField(max_length=50)),
                ('id_categoria', models.ForeignKey(blank=True, null=True, to='movimiento_dinero.Categoria')),
                ('id_persona', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
    ]
