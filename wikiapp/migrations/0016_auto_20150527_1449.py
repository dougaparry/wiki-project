# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0015_auto_20150527_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_articleID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_contentID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
