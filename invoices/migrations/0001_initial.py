# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_paid', models.DateField(blank=True)),
                ('date_shipped', models.DateField(blank=True)),
                ('tracking_number', models.CharField(max_length=128, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('customer', models.ForeignKey(to='customers.Customer')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
