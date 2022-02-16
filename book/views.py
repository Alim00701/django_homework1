from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse, redirect
# from django.http import HttpResponse


def get_books_all(request):
    books = models.Books.objects.all()
    return render(request, "books_list.html", {"books": books})


def get_books_detail(request, id):
    book = get_object_or_404(models.Books, id=id)
    comment_id = models.BookComments.objects.filter(books_id=id)
    return render(request, "books_detail.html", {"book": book, 'comment': comment_id})


def all_books(request):
    method = request.method
    if method == "POST":
        form = forms.Books_all(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:books_list"))
            # return HttpResponse("Books Created Successfully")
    else:
        form = forms.Books_all()
    return render(request, "add_books.html", {"form": form})
