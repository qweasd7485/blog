from django.contrib import admin
from article.models import Article, Comment

# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display=['title', 'content', 'likes']
    
    class Meta:
        model = Article

class CommentModelAdmin(admin.ModelAdmin):
    list_display=['article', 'content']
    list_display_links = ['article']
    admin_filter_links = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']
    
    class Meta:
        model = Comment

admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
