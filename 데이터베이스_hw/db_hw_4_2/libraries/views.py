from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'libraries/index.html', {'books': books})

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'libraries/detail.html', {'book': book})