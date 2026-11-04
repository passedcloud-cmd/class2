from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    authors = Author.objects.all()          # 저자 전부 가져오기
    context = {'authors': authors}
    return render(request, 'libraries/index.html', context)

def detail(request, pk):
    author = Author.objects.get(pk=pk)      # pk번 저자 한 명 가져오기
    context = {'author': author}
    return render(request, 'libraries/detail.html', context)