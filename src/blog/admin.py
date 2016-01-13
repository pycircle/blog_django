from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'author', 'updated']
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
