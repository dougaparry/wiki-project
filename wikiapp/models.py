# Date 28th May
# Group: Charne, Cleo, Doug, Jess

from django.db import models
import datetime

# Model to create articles, foreign key connection to content
class Article(models.Model):
	article_articleID = models.AutoField(primary_key = True)

	article_title = models.CharField(max_length=100, unique=True)
	article_continent = models.CharField(max_length=20, blank=True)
	article_last_revision = models.OneToOneField('Content', null=True, blank=True)
	article_author = models.CharField(max_length=100, blank=False, default='')

	def __unicode__(self):
		return self.article_title

# Model to create content, many to one article. Used for rollbacks
class Content(models.Model):
	content_contentID = models.AutoField(primary_key=True)

	content_content = models.TextField(blank=True)
	content_article = models.ForeignKey('Article')
	content_change_date = models.DateTimeField(null=True)
	content_author = models.CharField(max_length=100, blank=False, default='')

	def __unicode__(self):
		return self.content_article.article_title +  " " + str(self.content_change_date)
