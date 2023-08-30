from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils.timezone import now


class Books(models.Model):
    id = models.AutoField
    book_name = models.CharField(max_length=10000)
    img = models.ImageField(upload_to="images", default="")
    # imgall = models.ImageField(default="", blank=True)
    book_desc = RichTextField()
    # book_desc = models.TextField(max_length=10000000000, blank=True)

    def __str__(self):
        return self.book_name


class Audio(models.Model):
    id = models.AutoField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story_name = models.CharField(max_length=10000)
    story_audio = models.FileField(upload_to="audio", default="")
    # book_title = models.TextField(max_length=200)

    def __str__(self):
        return self.story_name


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Books, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.post
