# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_persona_id_matrimonio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
