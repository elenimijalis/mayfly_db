# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_paper_lookup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='pdf',
        ),
    ]
