# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pizza_name', models.CharField(max_length=20)),
                ('quantity', models.DecimalField(max_digits=10, decimal_places=0)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
