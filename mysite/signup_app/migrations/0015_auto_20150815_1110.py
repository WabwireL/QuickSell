# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0014_auto_20150815_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
