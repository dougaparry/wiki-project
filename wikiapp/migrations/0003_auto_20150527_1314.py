# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0002_auto_20150527_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_last_revision',
            field=models.ForeignKey(to='wikiapp.Content'),
        ),
    ]
