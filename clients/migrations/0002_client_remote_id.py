# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='remote_id',
            field=models.IntegerField(default=0, verbose_name='Zdalne id'),
            preserve_default=False,
        ),
    ]
