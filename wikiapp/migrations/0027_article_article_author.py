# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0026_auto_20150527_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
