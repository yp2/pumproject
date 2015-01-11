# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_auto_20150111_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='author',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
    ]
