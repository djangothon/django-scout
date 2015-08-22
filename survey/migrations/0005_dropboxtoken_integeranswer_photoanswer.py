# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropboxToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dropbox_token', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntegerAnswer',
            fields=[
                ('baseanswer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.BaseAnswer')),
                ('number', models.IntegerField()),
            ],
            bases=('survey.baseanswer',),
        ),
        migrations.CreateModel(
            name='PhotoAnswer',
            fields=[
                ('baseanswer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.BaseAnswer')),
                ('image_url', models.URLField()),
            ],
            bases=('survey.baseanswer',),
        ),
    ]
