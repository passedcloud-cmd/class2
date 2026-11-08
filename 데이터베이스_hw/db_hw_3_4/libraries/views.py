from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Author
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm() 
    context = {
        'author': author,
        'book_form': book_form,
    }
    return render(request, 'libraries/detail.html', context)

@require_POST
def book_create(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    book_form = BookForm(request.POST)   # 사용자가 입력한 데이터를 폼에 담기

    if book_form.is_valid():             # 입력값 검사 통과하면
        book = book_form.save(commit=False)  # ① DB 저장은 잠깐 보류!
        book.author = author                 # ② 저자를 직접 채워 넣고
        book.save()                          # ③ 이제 진짜 저장
        return redirect('libraries:detail', author.pk)

    # 입력값이 이상하면: 에러가 담긴 폼을 들고 상세 페이지를 다시 보여줌
    context = {
        'author': author,
        'book_form': book_form,
    }
    return render(request, 'libraries/detail.html', context)