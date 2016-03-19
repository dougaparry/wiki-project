from django.contrib import admin
from .models import Article, Content

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('article_title', 'article_continent')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Content)

