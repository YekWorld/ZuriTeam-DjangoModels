from django.contrib import admin
from .models import blog_post
# Register your models here.

class blog_postDB(admin.ModelAdmin):
    list_display = [
        "blog_title", "blog_text", "blog_author", "blog_date", "Publish_year"
   ]

