# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0020_auto_20150527_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_change_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
