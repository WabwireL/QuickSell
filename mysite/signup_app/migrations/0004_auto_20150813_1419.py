# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0003_auto_20150813_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='date_of_birth',
            field=models.DateField(verbose_name=b'dob'),
        ),
    ]
