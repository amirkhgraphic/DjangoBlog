from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from apps.posts.models import Category, Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ['created_at', 'user', 'post']
    fields = ['user', 'body', 'created_at']


class PostInline(admin.StackedInline):
    model = Post
    readonly_fields = ['author', 'created_at', 'last_modified']
    fields = ['title', 'body', 'author', 'created_at', 'last_modified']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    fields = ['name']
    inlines = [PostInline]
    search_fields = ['name']
    ordering = ['name']
    add_fieldsets = (
        (_('Required Fields'), {'classes': ['wide'], 'fields': ['name']}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'last_modified']
    list_filter = ['category', 'author']
    fields = ['title', 'body', 'author', 'category', 'created_at', 'last_modified']
    inlines = [CommentInline]
    readonly_fields = ['author', 'created_at', 'last_modified']
    search_fields = ['title', 'body']
    ordering = ['-created_at', '-last_modified']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    list_filter = ['user', 'post']
    fields = ['user', 'post', 'body', 'created_at']
    readonly_fields = ['created_at']
    search_fields = ['body']
    ordering = ['-created_at']
