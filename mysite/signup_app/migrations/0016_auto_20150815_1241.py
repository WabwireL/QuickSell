# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0015_auto_20150815_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]
