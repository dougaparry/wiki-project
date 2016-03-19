# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0016_auto_20150527_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_last_revision',
            field=models.OneToOneField(null=True, to='wikiapp.Content'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_article_id',
            field=models.ForeignKey(to='wikiapp.Article'),
        ),
    ]
