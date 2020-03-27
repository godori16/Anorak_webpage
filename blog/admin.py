from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)