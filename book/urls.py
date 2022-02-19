from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('books/', views.get_books_all, name="books_list"),
    path('books/<int:id>/', views.get_books_detail, name="books_detail"),
    path('books/<int:id>/update/', views.put_books_update, name="books_update"),
    path('books/<int:id>/delete/', views.book_delete, name="books_delete"),
    path('add-books/', views.all_books, name="add_books")
]
