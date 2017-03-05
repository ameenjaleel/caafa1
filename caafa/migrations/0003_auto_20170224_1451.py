# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafa', '0002_auto_20170216_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodcort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=250)),
                ('product_img', models.ImageField(upload_to=b'')),
                ('product_about', models.TextField()),
                ('product_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
