from django.contrib import admin

from core.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content", "tags__name")
    list_filter = ("created_at", "tags")
    date_hierarchy = "created_at"

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
