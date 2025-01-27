from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model for authors
    """
    full_name = models.CharField(max_length=250, unique=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.full_name}'


class Book(models.Model):
    """
    Model Representing a book title
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, editable=True)
    subtitle = models.CharField(max_length=250, unique=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    source = models.URLField(
        max_length=200, blank=True
    )
    synopsis = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_published = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True
        )
    
    def __str__(self):
        return f'{self.title} by {self.author} ({self.first_published})'


class Section(models.Model):
    """
    Model to represent the section of a book such as a page or chapter (book depending)
    """
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250, editable=True)
    subtitle = models.CharField(max_length=250, editable=True, null=True)
    slug = models.SlugField(max_length=250, editable=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.book} Section {self.id}: {self.name}'