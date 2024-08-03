from django.contrib import admin
from .models import Article, Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'created_at', 'is_active')
    list_filter = ('author', 'created_at', 'is_active')
    search_fields = ('comment',)
    date_hierarchy = 'created_at'
    actions = ['disable_comment', 'enable_comment']
    readonly_fields = ('author', 'created_at',)

    def disable_comment(self, queryset):
        queryset.update(is_active=False)

    def enable_comment(self, queryset):
        queryset.update(is_active=True)


admin.site.register(Comment, CommentAdmin)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'body', 'author')
    date_hierarchy = 'created_at'
    readonly_fields = ('author', 'created_at',)
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
