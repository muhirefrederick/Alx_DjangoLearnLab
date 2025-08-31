# Django Book Model CRUD Operations

## 1. Create Book

```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Check the book
book
# Expected Output: <Book: 1984 by George Orwell (1949)>

from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Expected Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

from bookshelf.models import Book

# Get the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check updated book
book
# Expected Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output: <QuerySet []>
