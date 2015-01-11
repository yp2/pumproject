# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=150, blank=True)),
                ('author', models.CharField(default=b'', max_length=150, blank=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
    ]
