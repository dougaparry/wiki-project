# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0006_auto_20150527_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_content',
        ),
    ]
