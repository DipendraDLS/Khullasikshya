from django.db import models


# Create your models here.
class Level(models.Model):
    level_name = models.CharField(max_length=200, unique=True)
    level_image = models.ImageField(null=True, blank=True, upload_to='uploads')
    level_order = models.IntegerField(default=1)
    level_created_at = models.DateTimeField(auto_now_add=True, null=True)
    level_updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.objects.all()

    # This is for image field as while adding level if admin doesn't choose any photo then error will appear as image field is not made required
    # so in order to tackel with The 'photo' attribute has no file associated with it error we did this.
    @property
    def photo_url(self):
        if self.level_image and hasattr(self.level_image, 'url'):
            return self.level_image.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/logo_black.png"


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200, unique=True)
    faculty_description = models.TextField(null=True, max_length=500)
    faculty_image = models.ImageField(null=True, blank=True, upload_to='uploads')
    level = models.ForeignKey("Level", on_delete=models.SET_NULL, null=True)
    faculty_created_at = models.DateTimeField(auto_now_add=True, null=True)
    faculty_updated_at = models.DateTimeField(auto_now=True, null=True)

    # This is for image field as while adding level if admin doesn't choose any photo then error will appear as image field is not made required
    # so in order to tackel with The 'photo' attribute has no file associated with it error we did this.
    @property
    def photo_url(self):
        if self.faculty_image and hasattr(self.faculty_image, 'url'):
            return self.faculty_image.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/logo_black.png"


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_description = models.TextField(null=True, max_length=500)
    subject_image = models.ImageField(null=True, blank=True, upload_to='uploads')
    subject_semester = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    faculty = models.ForeignKey("Faculty", on_delete=models.SET_NULL, null=True)
    subject_order = models.IntegerField(default=1)

    def __str__(self):
        return self.objects.all()

    @property
    def photo_url(self):
        if self.subject_image and hasattr(self.subject_image, 'url'):
            return self.subject_image.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/subject_logo.png"


class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_description = models.TextField(null=True, blank=True, max_length=500)
    note_created_at = models.DateTimeField(auto_now_add=True, null=True)
    note_updated_at = models.DateTimeField(auto_now=True, null=True)
    document = models.FileField(upload_to='notes/')
    document_cover = models.ImageField(null=True, blank=True, upload_to='notes_cover/')
    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.note_name

    @property
    def photo_url(self):
        if self.document_cover and hasattr(self.document_cover, 'url'):
            return self.document_cover.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/document_cover_logo.png"


class Syllabus(models.Model):
    syllabus_title = models.CharField(max_length=200)
    syllabus_description = models.TextField(null=True, blank=True, max_length=500)
    syllabus_created_at = models.DateTimeField(auto_now_add=True, null=True)
    syllabus_updated_at = models.DateTimeField(auto_now=True, null=True)
    document = models.FileField(upload_to='syllabus/')
    document_cover = models.ImageField(null=True, blank=True, upload_to='syllabus_cover/')
    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.note_name

    @property
    def photo_url(self):
        if self.document_cover and hasattr(self.document_cover, 'url'):
            return self.document_cover.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/document_cover_logo.png"


class PastQuestion(models.Model):
    pq_title = models.CharField(max_length=200)
    pq_description = models.TextField(null=True, blank=True, max_length=500)
    pq_created_at = models.DateTimeField(auto_now_add=True, null=True)
    pq_updated_at = models.DateTimeField(auto_now=True, null=True)
    document = models.FileField(upload_to='past_question/')
    document_cover = models.ImageField(null=True, blank=True, upload_to='pq_cover/')

    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pq_title

    @property
    def photo_url(self):
        if self.document_cover and hasattr(self.document_cover, 'url'):
            return self.document_cover.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/document_cover_logo.png"


class PastQuestionSolution(models.Model):
    pqs_title = models.CharField(max_length=200)
    pqs_description = models.TextField(null=True, blank=True, max_length=500)
    pqs_created_at = models.DateTimeField(auto_now_add=True, null=True)
    pqs_updated_at = models.DateTimeField(auto_now=True, null=True)
    pqs_order = models.IntegerField(null=True)
    document = models.FileField(upload_to='past_question_solution/')
    document_cover = models.ImageField(null=True, blank=True, upload_to='pqs_cover/')
    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pqs_title

    @property
    def photo_url(self):
        if self.document_cover and hasattr(self.document_cover, 'url'):
            return self.document_cover.url
        # If admin didn't choose any photo while adding level then default photo will be shown.
        else:
            return "/static/images/document_cover_logo.png"
