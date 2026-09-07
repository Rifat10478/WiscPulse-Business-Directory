from django.contrib import admin

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

 list_display = (
    "title",
    "event_date",
    "event_time",
    "location",
    "status",
)

 list_filter = (
    "status",
    "event_date",
)

 search_fields = (
    "title",
    "description",
    "location",
)

 prepopulated_fields = {
    "slug": ("title",)
}

 readonly_fields = (
    "created_at",
    "updated_at",
)

