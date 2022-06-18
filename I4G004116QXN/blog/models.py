from django.db import models
from tabnanny import verbose
from turtle import title
from django.contrib.auth import get_user_model
# Create your models here.

class blog_post(models.Model):
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Post"
    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField()
    blog_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blog_date = models.DateTimeField()
    Published_year = models.DateTimeField()


# Create your models here.
