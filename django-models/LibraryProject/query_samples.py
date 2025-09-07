import os
import django

# Set the correct settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
# 1. Query all books  in the database.
def query_all_books():
    books = Book.objects.all()
    for book in books:
        print(f"Book Title: {book.title}, Author: {book.author.name}")


