from django.contrib import admin
from .models import Article, Comment

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date", "updated_date", 'active']
    list_display_links = ["title", "created_date"]
    search_fields = ["title", "content"]
    list_filter = ['active', "created_date", "author"]
    actions = ['makale_onayla']

    def makale_onayla(self, request, queryset):
        queryset.update(active=True)

    class Meta:
        model = Article

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author','email', 'comment_content', 'article', 'comment_date', 'active')
    list_filter = ('active', 'comment_date')
    search_fields = ('comment_author', 'email', 'comment_content')
    actions = ['yorum_onayla']

    def yorum_onayla(self, request, queryset):
        queryset.update(active=True)

    class Meta:
        model = Comment