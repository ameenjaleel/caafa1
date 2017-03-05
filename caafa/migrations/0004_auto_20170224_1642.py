# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafa', '0003_auto_20170224_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcort',
            name='product_img',
            field=models.ImageField(upload_to=b'caafa/img'),
        ),
    ]
