# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150822_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseanswer',
            name='answer',
        ),
        migrations.AddField(
            model_name='baseanswer',
            name='uid',
            field=models.CharField(default=1, unique=True, max_length=15, db_index=True),
            preserve_default=False,
        ),
    ]
