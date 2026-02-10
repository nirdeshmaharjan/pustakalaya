from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_page")
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



def login_view(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username = username)
            if not user.exists():
                messages.success(request,"user not found")
                return redirect('/login/')
            user = authenticate(username = username , password = password)
            print(user)
            if not user:
                messages.success(request , "Incorrect password")

                return redirect('/login/')
            login(request , user)
            return redirect('/')

    return render(request,"login.html" )



def logout_view(request):
    logout(request)
    return redirect('/login/')



def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')


        user = User.objects.filter(username = username)
        if user.exists():
           messages.success(request,"username already taken")
           return redirect('/register/')
        
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save()
        messages.success(request,"Account Created")
        return redirect('/register/')

        




    return render(request,"register.html" )