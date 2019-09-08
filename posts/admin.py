from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)
