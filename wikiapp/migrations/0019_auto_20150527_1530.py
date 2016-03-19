# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0018_auto_20150527_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_last_revision',
            field=models.OneToOneField(blank=True, null=True, to='wikiapp.Content'),
        ),
    ]
