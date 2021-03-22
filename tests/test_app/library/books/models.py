from django.db import models
from django.urls import reverse

from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    library = models.ForeignKey("loans.Library", related_name="books", on_delete=models.CASCADE)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text=(
            "13 Character " '<a href="https://www.isbn-international.org/content/what-isbn">' "ISBN number</a>",
        ),
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    published_on = models.DateField()

    def get_absolute_url(self):
        return reverse("admin:books_book_change", args=(self.id,))

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ("last_name", "first_name")

    def get_absolute_url(self):
        return reverse("admin:books_author_change", args=(self.id,))

    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)
