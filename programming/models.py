from django.db import models
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Programming(models.Model):
    language_type = models.CharField(max_length=100, unique=True)


class ProgrammingLanguage(models.Model):
    p_title = models.CharField(max_length=100)
    p_code = RichTextUploadingField(blank=True, null=True)
    p_link = models.CharField(max_length=500)
    p_language = models.ForeignKey(Programming, on_delete=models.CASCADE, related_name='programming_type')

    def __unicode__(self):
        return "%s" % self.p_language
