from django.db import models

# Create your models here.
class video(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to="videos")
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

