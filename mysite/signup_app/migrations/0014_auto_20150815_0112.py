# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0013_auto_20150815_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email_adress',
            field=models.EmailField(max_length=100),
        ),
    ]
