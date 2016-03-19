# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0014_auto_20150527_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_id',
            new_name='article_articleID',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content_id',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content_page_id',
        ),
        migrations.AddField(
            model_name='content',
            name='content_article_id',
            field=models.ForeignKey(null=True, to='wikiapp.Article'),
        ),
        migrations.AddField(
            model_name='content',
            name='content_change_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='content_content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='content_contentID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_continent',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_last_revision',
            field=models.ForeignKey(null=True, to='wikiapp.Content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
