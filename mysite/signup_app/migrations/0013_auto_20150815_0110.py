# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0012_auto_20150815_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
    ]
