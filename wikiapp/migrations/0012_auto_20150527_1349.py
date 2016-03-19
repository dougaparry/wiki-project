# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0011_auto_20150527_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_last_revision',
            field=models.ForeignKey(default=0, to='wikiapp.Content'),
        ),
    ]
