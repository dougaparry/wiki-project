# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_change_date',
            field=models.DateTimeField(),
        ),
    ]
