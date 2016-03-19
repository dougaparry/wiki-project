# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0003_auto_20150527_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_change_date',
        ),
    ]
