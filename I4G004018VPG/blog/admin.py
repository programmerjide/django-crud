from django.contrib import admin

# Register your models here.

# Register the post model
from blog.models import Post
admin.site.register(Post)


