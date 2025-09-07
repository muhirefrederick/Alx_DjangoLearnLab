from bookshelf.models import Book

# Get the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check updated book
book
# Expected Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
