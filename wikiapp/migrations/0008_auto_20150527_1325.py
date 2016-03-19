# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0007_remove_content_content_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_page_id',
        ),
        migrations.AddField(
            model_name='content',
            name='content_page_id',
            field=models.ForeignKey(default=0, to='wikiapp.Article'),
        ),
    ]
