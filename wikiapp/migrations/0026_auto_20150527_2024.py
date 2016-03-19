# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0025_auto_20150527_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
