from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def book_index(request):
    all_books= Book.objects.all()
    return render(request, "book/book_index.html", context={
        "books":all_books
    })

def book_details(request, pk):
    book= Book.objects.get(pk=pk)
    return render(request, "book/book_details.html", context={
        "book": book
    })

def book_delete(request, pk):
    Book.objects.get(pk= pk).delete()
    return redirect("book:book-index")

def book_create(request):
    form= BookForm()
    if request.method == "POST":
        form= BookForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect("book:book-index")
    return render(request, "book/book_create.html", context={
        "form": form
    })

def book_update(request, pk):
    book= Book.objects.get(pk=pk)
    form= BookForm(instance= book)
    if request.method== "POST":
        form= BookForm(instance= form, data= request)
        if form.is_valid():
            form.save()
            return redirect("book:book-index")
    return render(request, 'book/book_update.html', context={
        'form': form,
        'book' : book
    })

# Create your views here.
