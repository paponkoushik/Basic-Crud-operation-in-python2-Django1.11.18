# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . models import BookList
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def resetPass(request):
    return render(request, 'reset_pass.html')

def addBook(request):
    return render(request, 'add_book.html')

def createBook(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/login/')

def login(request):
    books = BookList.objects.all()
    return render(request, 'dashbord.html', {'books':books})

def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/login/')

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)

def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/login/')