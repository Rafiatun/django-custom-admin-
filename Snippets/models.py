from django.db import models

# Create your models here.

class snippet(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    font_size=models.IntegerField(default=14)


    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]