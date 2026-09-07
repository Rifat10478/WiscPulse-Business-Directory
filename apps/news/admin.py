from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):


 list_display = (
    "title",
    "status",
    "created_at",
)

 list_filter = (
    "status",
    "created_at",
)

 search_fields = (
    "title",
    "short_description",
    "content",
)

 prepopulated_fields = {
    "slug": ("title",)
}

 readonly_fields = (
    "created_at",
    "updated_at",
)

