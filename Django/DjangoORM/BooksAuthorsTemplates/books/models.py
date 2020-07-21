from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors =>
    # some_book.authors.add(some_author)


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField('Book', related_name='authors')
    # some_author_books.add(some_book)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
