# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('topping', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('basepizza', models.ForeignKey(to='pizza.Pizza')),
            ],
        ),
    ]
