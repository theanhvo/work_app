from django.contrib import admin
from .models import Post, Job


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post,  PostAdmin)


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
