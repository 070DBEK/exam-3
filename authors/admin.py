from django.contrib import admin
from .models import Author
from django.contrib.admin import DateFieldListFilter


@admin.action(description='Mark authors as active')
def mark_as_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "slug", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "bio")
    list_filter = (
        ("birth_date", DateFieldListFilter),
        "created_at",
        "updated_at",
    )
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    ordering = ("last_name", "-created_at")
    fields = ("first_name", "last_name", "profile_picture", "bio", "birth_date", "slug")
    readonly_fields = ("created_at", "updated_at")
    actions = [mark_as_active]
