# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('article_title', models.CharField(blank=True, max_length=b'100')),
                ('article_continent', models.CharField(blank=True, max_length=b'20')),
                ('article_last_revision', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('content_content', models.TextField(blank=True)),
                ('content_change_date', models.DateTimeField(verbose_name=b'date published')),
                ('content_page_id', models.ForeignKey(to='wikiapp.Article')),
            ],
        ),
    ]
