from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


def get_books_all(request):
    books = models.Books.objects.all()
    return render(request, "books_list.html", {"books": books})


def get_books_detail(request, id):
    book = get_object_or_404(models.Books, id=id)
    comment_id = models.BookComments.objects.filter(books_id=id)
    return render(request, "books_detail.html", {"book": book,'comment':comment_id})
