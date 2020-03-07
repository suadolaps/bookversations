from django.db import models
from django.utils import timezone


class ReadingList(models.Model):
    book_title = models.CharField(max_length=250)
    book_blurb = models.CharField(max_length=1000)
    book_image = models.ImageField(upload_to='images/book_covers/', null=True)

    def __str__(self):
        return self.book_title


class Subscribe(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
