# bookstore/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Action', 'Action'),
        ('Survey', 'Survey'),
        # Add more categories here if needed
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    saleprice = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # New field

    def __str__(self):
        return self.title
