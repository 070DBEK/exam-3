from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "slug", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "bio")
    list_filter = ("birth_date", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    ordering = ("last_name", "-created_at")
    fields = ("first_name", "last_name", "bio", "birth_date", "slug")
    readonly_fields = ("created_at", "updated_at")
