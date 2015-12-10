# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_paper_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
