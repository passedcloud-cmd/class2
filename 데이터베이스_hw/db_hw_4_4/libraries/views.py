from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from django.views.decorators.http import require_POST
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book': book,
        'review_form': ReviewForm(),
        'reviews': book.review_set.all(), 
    }
    return render(request, 'libraries/detail.html', context)

@require_POST
def review_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    book = get_object_or_404(Book, pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book              
        review.user = request.user      
        review.save()
    return redirect('libraries:detail', book.pk)


@require_POST
def review_delete(request, book_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:     
        review.delete()
    return redirect('libraries:detail', book_pk)