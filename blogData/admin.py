from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
 list_filter = ('author', 'tags', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "date", "email")
    list_filter = ("post", "date")
    search_fields = ("name", "text", "email")

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
