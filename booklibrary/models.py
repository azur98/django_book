from django.db import models

class BookModel(models.Model):
    bookname = models.CharField(max_length = 50)
    summary = models.TextField()
    rating = models.IntegerField()
