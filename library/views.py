from django.shortcuts import render, get_object_or_404
from .models import Book, Section

# Create your views here.


def library(request):
    """
    A view to return the library page.
    """
    books = Book.objects.all

    # Create a context dictionary to pass data to the template
    context = {
        'books': books,
    }

    # Render the index page with the provided context
    return render(request, 'library/library.html', context)


def book(request, slug):
    """
    A view to start reading
    """

    book = get_object_or_404(Book, slug=slug)
    sections = Section.objects.filter(book=book)

    # Create a context dictionary to pass data to the template
    context = {
        'book' : book,
        'sections' : sections,
    }

    # Render the book template with the context data
    return render(request, 'library/book.html', context)


def section(request, book_slug, slug):
    """
    A view for each section/chapter
    """

    book = get_object_or_404(Book, slug=book_slug)
    section = get_object_or_404(Section, slug=slug)

        # Create a context dictionary to pass data to the template
    context = {
        'book' : book,
        'section' : section,
    }

    # Render the book template with the context data
    return render(request, 'library/section.html', context)


