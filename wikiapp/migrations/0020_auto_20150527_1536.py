# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0019_auto_20150527_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='content_article_id',
            new_name='content_article',
        ),
    ]
