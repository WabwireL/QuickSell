# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0009_auto_20150815_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email_adress',
            field=models.EmailField(max_length=100),
        ),
    ]
