# bookstore/admin.py
from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'saleprice', 'image')
    search_fields = ('title', 'author__name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
