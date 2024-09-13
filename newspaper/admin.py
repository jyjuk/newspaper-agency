from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, Newspaper, Redactor

admin.site.register(Topic)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = [
        "topic",
        "title",
        "published_date",
        "display_authors"
    ]
    search_fields = ["topic", "title"]
    list_filter = ["topic", "published_date"]


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("years_of_experience",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": ("first_name", "last_name", "years_of_experience",)
            }
        ),
    )
    list_filter = UserAdmin.list_filter + ("years_of_experience",)
