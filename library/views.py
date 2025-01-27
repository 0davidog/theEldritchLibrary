from django.shortcuts import render

# Create your views here.


def library(request):
    """
    A view to return the library page.
    """
    # Render the index page with the provided context
    return render(request, 'library/library.html')