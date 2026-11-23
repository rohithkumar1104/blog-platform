from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from unfold.admin import ModelAdmin
from .models import Post, Category, AboutUs

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "category", "user", "created_at")
    list_filter = ("category",)
    search_fields = ("title",)

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    pass