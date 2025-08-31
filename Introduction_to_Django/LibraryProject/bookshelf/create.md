# Django Book Model CRUD Operations

## 1. Create Book

```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Check the book
book
# Expected Output: <Book: 1984 by George Orwell (1949)>
