from django.contrib import admin

from .models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "city",
        "rating",
        "review_count",
        "status",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "status",
        "is_featured",
        "category",
        "city",
    )

    search_fields = (
        "name",
        "description",
        "city",
        "address",
        "phone",
        "email",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "status",
        "is_featured",
    )

    ordering = (
        "-created_at",
    )