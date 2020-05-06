from django.db import models


class ReadingList(models.Model):
    book_title = models.CharField(max_length=250)
    book_blurb = models.TextField()
    book_image = models.ImageField(upload_to='images/book_covers/', null=True)

    def __str__(self):
        return self.book_title

    @property
    def book_image_url(self):
        if self.book_image and hasattr(self.book_image, 'url'):
            return self.book_image.url
        return '#'


class NewsletterUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
