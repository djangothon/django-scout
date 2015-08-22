# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answertype',
            name='dec_number',
        ),
        migrations.RemoveField(
            model_name='answertype',
            name='image',
        ),
        migrations.RemoveField(
            model_name='answertype',
            name='int_number',
        ),
        migrations.RemoveField(
            model_name='answertype',
            name='location',
        ),
        migrations.RemoveField(
            model_name='answertype',
            name='text',
        ),
    ]
