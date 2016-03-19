# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0004_remove_content_content_change_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_page_id',
        ),
        migrations.AddField(
            model_name='content',
            name='content_page_id',
            field=models.ManyToManyField(to='wikiapp.Article'),
        ),
    ]
