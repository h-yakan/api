from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    pageNum = models.IntegerField()
    publishDate = models.DateField()

    def __str__(self):
        return f"{self.title}"