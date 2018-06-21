from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('url','user','time_created','likes')
admin.site.register(Post, PostAdmin)
