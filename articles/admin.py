from django.contrib import admin
from .models import *


# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    inlines = [CommentInline]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
