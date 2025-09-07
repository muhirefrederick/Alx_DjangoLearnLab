from django.contrib import admin
from .models import Book

# Register the Book model
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    search_fields = ('title', 'author')                     # enable search by title or author
    list_filter = ('publication_year',)
    
