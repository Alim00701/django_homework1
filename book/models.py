from django.db import models


class Books(models.Model):
    GENRE_CHOICE = (
        ("Romantic", "Romantic"),
        ("Drama", "Drama"),
        ("Historical", "Historical"),
        ("Comedy", "Comedy"),
        ("Horror", "Horror"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(max_length=60, choices=GENRE_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class BookComments(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE,
                              related_name="books_comments")


class Book_shop(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    author = models.CharField(max_length=70)


class BookFeedback(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    book_comment = models.ForeignKey(Book_shop, on_delete=models.CASCADE,
                                     related_name="book_comment")
