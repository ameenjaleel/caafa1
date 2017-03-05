# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodcort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resto_name', models.CharField(max_length=250)),
                ('product_rest', models.CharField(max_length=250)),
                ('product_name', models.CharField(max_length=250)),
                ('product_cuisines', models.CharField(max_length=250, blank=True)),
                ('product_img', models.FileField(null=True, upload_to=b'', blank=True)),
                ('product_about', models.TextField()),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
