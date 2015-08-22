# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('image', models.ImageField(null=True, upload_to=b'images//%Y/%m/%d/', blank=True)),
                ('text', models.CharField(max_length=500, null=True, blank=True)),
                ('int_number', models.IntegerField(null=True, blank=True)),
                ('dec_number', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(to='survey.AnswerType')),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LatLngType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.CharField(max_length=20, null=True, verbose_name=b'Latitude', blank=True)),
                ('longitude', models.CharField(max_length=20, null=True, verbose_name=b'Longitude', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=15, db_index=True)),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer_type', models.ForeignKey(to='survey.AnswerType')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=15, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('public', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='survey.Question')),
            ],
        ),
        migrations.AddField(
            model_name='baseanswer',
            name='question',
            field=models.ForeignKey(editable=False, to='survey.Question'),
        ),
        migrations.AddField(
            model_name='answertype',
            name='location',
            field=models.ForeignKey(blank=True, to='survey.LatLngType', null=True),
        ),
    ]
