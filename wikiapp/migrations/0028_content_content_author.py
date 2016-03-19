# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0027_article_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_author',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
