# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20151110_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='lookup',
            field=models.CharField(default=b'', max_length=32),
        ),
    ]
