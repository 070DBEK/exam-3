from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name", )
    list_filter = ("created_at", "updated_at")
    prepopulated_fields = {"slug" : ("name", )}
    ordering = ("name", "-created_at")
    fields = ("name", "slug")
    readonly_fields = ("created_at", "updated_at")

