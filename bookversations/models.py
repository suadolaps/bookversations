from django.db import models

# Create your models here.
class ReadingList(models.Model):
    book = models.ImageField()
    book_name = models.CharField(max_length=250)
    book_blurb = models.CharField(max_length=1000)

    def __str__(self):
        return self.book_name