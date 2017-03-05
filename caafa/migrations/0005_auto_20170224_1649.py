# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafa', '0004_auto_20170224_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcort',
            name='product_img',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
