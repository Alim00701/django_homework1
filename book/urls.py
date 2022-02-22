from django.urls import path
from . import views, models

app_name = "books"
urlpatterns = [
    path('books/', views.BooksListView.as_view(), name="books_list"),
    path('books/comedy/', views.BooksListView.as_view(queryset=models.Books.objects.filter(genre="Comedy").order_by("-created_date")), name="books_comedy_list"),
    path('books/horror/', views.BooksListView.as_view(queryset=models.Books.objects.filter(genre="Horror").order_by("-created_date")), name="books_horror_list"),
    path('books/drama/', views.BooksListView.as_view(queryset=models.Books.objects.filter(genre="Drama").order_by("-created_date")), name="books_drama_list"),
    path('books/<int:id>/', views.BooksDetailView.as_view(), name="books_detail"),
    path('books/<int:id>/update/', views.BooksUpdateView.as_view(), name="books_update"),
    path('books/<int:id>/delete/', views.BooksDeleteView.as_view(), name="books_delete"),
    path('add-books/', views.BooksCreateView.as_view(), name="add_books")
]
