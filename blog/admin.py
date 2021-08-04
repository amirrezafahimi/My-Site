from django.contrib import admin

from .models import Author, Post, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tags")
    list_display = ("title", "date", "author")
    prepopulated_fields = {
        "slug": ("title",)
    }


admin.site.register(Author)
# admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
