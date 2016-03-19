# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0024_auto_20150527_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=100),
        ),
    ]
