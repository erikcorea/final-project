from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    def has_change_permission(request, obj=None):
        return obj.author == request.user

admin.site.register(Post, PostAdmin)