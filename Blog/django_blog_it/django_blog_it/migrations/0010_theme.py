# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0009_contactussettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
    ]
