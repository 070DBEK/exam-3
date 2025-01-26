from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "catalog", "get_tags", "created_at", "updated_at")
    search_fields = ("title", "content", "author__first_name", "author__last_name", "tags__name")
    list_filter = ("created_at", "updated_at", "catalog", "author")
    ordering = ("title", "-created_at")
    fields = ("title", "content", "img", "author", "catalog", "tags")
    readonly_fields = ("created_at", "updated_at")

    def get_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    get_tags.short_description = "Tags"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'post')
    search_fields = ('content', 'author__first_name', 'author__last_name', 'post__title', 'email')
    ordering = ('-created_at',)
