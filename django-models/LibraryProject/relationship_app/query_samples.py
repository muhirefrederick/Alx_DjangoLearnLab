import os
import django

# Setup Django environment (point to your settings module)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Sample Data Creation
    author1, _ = Author.objects.get_or_create(name="Chinua Achebe")
    author2, _ = Author.objects.get_or_create(name="Ngugi wa Thiong'o")

    book1, _ = Book.objects.get_or_create(title="Things Fall Apart", author=author1)
    book2, _ = Book.objects.get_or_create(title="No Longer at Ease", author=author1)
    book3, _ = Book.objects.get_or_create(title="Petals of Blood", author=author2)

    library, _ = Library.objects.get_or_create(name="City Library")
    library.books.add(book1, book2, book3)

    librarian, _ = Librarian.objects.get_or_create(name="John Doe", library=library)

    # 1. Query all books by a specific author
    print("1. All books by Chinua Achebe:")
    for book in Book.objects.filter(author=author1):
        print("-", book.title)

    # 2. List all books in a library
    print("\n2. All books in City Library:")
    for book in library.books.all():
        print("-", book.title)

    # 3. Retrieve the librarian for a library
    print("\n3. Librarian for City Library:")
    print(library.librarian.name)


if __name__ == "__main__":
    run_queries()
