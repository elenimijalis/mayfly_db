# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_journal_orig_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='page_end',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AddField(
            model_name='paper',
            name='page_start',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AddField(
            model_name='paper',
            name='pdf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paper',
            name='reprint',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paper',
            name='url',
            field=models.URLField(default=b''),
        ),
        migrations.AddField(
            model_name='paper',
            name='volume',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='paper',
            name='keywords',
        ),
        migrations.AddField(
            model_name='paper',
            name='keywords',
            field=models.ManyToManyField(to='base.Keyword'),
        ),
    ]
