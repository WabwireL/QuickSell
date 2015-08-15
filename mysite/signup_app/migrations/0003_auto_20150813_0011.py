# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0002_auto_20150810_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='date_of_birth',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email_adress',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
