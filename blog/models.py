from django.db import models
from django.db import models
from login_signup.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=500)
    blog_created_at = models.DateTimeField(auto_now_add=True)
    blog_update_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blog_posts', default=True, null=True)
    blog_content = RichTextUploadingField(blank=True, null=True)
    blog_image = models.ImageField(upload_to='uploads/')


class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
