from django.db import models

# Create your models here


class Notice(models.Model):
    notice_title = models.CharField(max_length=500)
    notice_created_at = models.DateTimeField(auto_now_add=True)
    notice_content = models.TextField()
    notice_url = models.CharField(max_length=500)