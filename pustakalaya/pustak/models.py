from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    book_name=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    isbn_number=models.IntegerField()
    quantity=models.IntegerField()
    category=models.CharField(choices=(('Science','Science'),('Computer','Computer'),('Literature','Literature'),('Management','Management')),max_length=50  )
