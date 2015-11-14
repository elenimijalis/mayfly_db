# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151110_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='journal',
            field=models.ForeignKey(blank=True, to='base.Journal', null=True),
        ),
    ]
