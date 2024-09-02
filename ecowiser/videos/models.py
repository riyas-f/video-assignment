from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='videos/')
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
