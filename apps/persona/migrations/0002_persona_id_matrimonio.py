# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='id_matrimonio',
            field=models.ForeignKey(blank=True, null=True, to='persona.Matrimonio'),
        ),
    ]
