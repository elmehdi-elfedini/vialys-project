from django.contrib import admin
from .models import BlogPost, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    list_editable = ('published',)
    filter_horizontal = ('tags',)  

    actions = ['publish_posts', 'unpublish_posts']

    @admin.action(description='Publish selected posts')
    def publish_posts(self, request, queryset):
        queryset.update(published=True)

    @admin.action(description='Unpublish selected posts')
    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
