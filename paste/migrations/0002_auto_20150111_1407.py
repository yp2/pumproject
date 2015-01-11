# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='author',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
