from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    book_to_edit = None
    
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        
        if book_id:  
            book = Book.objects.get(id=book_id)
            book.name = request.POST.get('name')
            book.book_name = request.POST.get('book_name')
            book.author = request.POST.get('author')
            book.category = request.POST.get('category')
            book.isbn_number = request.POST.get('isbn_number')
            book.quantity = request.POST.get('quantity')
            book.save()
        else: 
            Book.objects.create(
                name=request.POST.get('name'),
                book_name=request.POST.get('book_name'),
                author=request.POST.get('author'),
                category=request.POST.get('category'),
                isbn_number=request.POST.get('isbn_number'),
                quantity=request.POST.get('quantity')
            )
        return redirect('book_list')
    
    edit_id = request.GET.get('edit')
    if edit_id:
        book_to_edit = Book.objects.get(id=edit_id)
    
    return render(request, 'index.html', {
        'books': books,
        'book_to_edit': book_to_edit
    })


def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('book_list')