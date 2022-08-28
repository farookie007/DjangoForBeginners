from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        n = 20                              # cut-off value for the text displayed
        return f"{self.text[:n] + '...' if len(self.text)>n else self.text}"
