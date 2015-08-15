# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='email_adress',
            field=models.EmailField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='date_of_birth',
            field=models.DateField(max_length=20),
        ),
    ]
