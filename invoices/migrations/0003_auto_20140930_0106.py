# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20140930_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_paid',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_shipped',
            field=models.DateField(null=True, blank=True),
        ),
    ]
