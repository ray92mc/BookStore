from django.shortcuts import render, get_object_or_404
from .models import Category, Book

# Create your views here.

def book_detail(request, category_id, book_id):

    try:
        book = Book.objects.get(category_id=category_id, id=book_id)
    except Exception as e:
        raise e

    return render(request, 'shop/book.html', {'book':book})

def allBookCat(request, category_id=None):
    c_page = None
    books = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        books = Book.objects.filter(category=c_page, availible=True)
        
    else:
        books = Book.objects.all().filter(availible=True)
   
    return render(request, 'shop/category.html', {'category':c_page,'books':books})


