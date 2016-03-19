# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0022_auto_20150527_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_change_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
