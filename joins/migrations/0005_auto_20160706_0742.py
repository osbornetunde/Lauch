# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_join_ref_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
