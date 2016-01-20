from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Article, Category, UserAbout


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'author', 'updated']
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    prepopulated_fields = {"slug": ("name",)}

class UserAboutInline(admin.StackedInline):
    model = UserAbout
    can_delete = False
    verbose_name_plural = 'About User'

class UserAdmin(BaseUserAdmin):
    inlines = (UserAboutInline, )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

# re-register user admin with new fields
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
