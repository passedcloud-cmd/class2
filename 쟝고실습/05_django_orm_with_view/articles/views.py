from django.shortcuts import render, redirect

from .models import Article


# Create your views here.
def index(request):
    """
    [메인 페이지]
    - 메인 페이지에는 전체 게시글 목록이 출력됨
    - 따라서 DB에서 전체 게시글을 가져와야 함
    - CRUD 중 READ : 전체 게시글 조회
    """
    # 1. DB에서 전체 게시글 조회
    #    - Article.objects.all() 의 결과는 QuerySet (게시글 객체들의 묶음)
    articles = Article.objects.all()

    # 2. 템플릿에 넘겨줄 데이터를 딕셔너리로 묶기
    #    - key('articles') => 템플릿에서 사용할 변수 이름
    #    - value(articles) => 실제로 전달되는 데이터
    context = {
        'articles': articles,
    }

    # 3. 템플릿(index.html)에 데이터(context)를 채워 HTML을 만들고, 응답으로 반환
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    """
    [단일 게시글 조회]
    -urls에서 넘겨받은 article_pk을 활용하여 몇 번 게시글을 조회할지 결정
    -DB에 단일 게시글 조회 후 
    - 변수에 담아서 템플릿과 함께 응답
    """

    # 1. 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)

    # 2. context에 담기
    context = {
        'article': article,
    }

    # 3. 템플릿과 함께 응답
    return render(request, 'articles/detail.html', context)

def new(request):
    """
    [게시글 작성 페이지]
    - 사용자 요청을 받아 게시글 데이터를 입력 받을 form이 담긴 페이지를 응답
    """
    return render(request, 'articles/new.html')


def create(request):
    """
    [실제로 게시글을 DB에 저장]
    """
    # 1. 사용자로부터 받은 제목과 내용을 추출
    title = request.POST.get('title') # 왼쪽 title은 변수이름일 뿐. # 오른쪽 title은 속성값. 둘은 이름이 같을 뿐 아무 연관 없음
    content = request.POST.get('content')

    # 2. Article 모델 클래스로 인스턴스를 생성 후 저장 과정 진행
    article = Article(title=title, content=content)
    article.save()

    # 3. 저장이 완료되었다는 걸 알리는 템플릿을 응답
    # return render(request, 'articles/create.html')

    # 3. 클라이언트가 상세 페이지로 다시 요청할 수 있도록 redirect 응답
    # redirect('태크:주소이름', 변수)
    return redirect('articles:detail', article.pk)

def delete(request, article_pk):
    """
    [특정 게시글 삭제]
    - 특정 게시글 조회를 먼저 진행
    - 조회 후 삭제
    """
    # 1. 게시글 조회
    article = Article.objects.get(pk=article_pk)

    # 2. 삭제
    article.delete()

    # 3. 사용자를 메인 페이지에 요청을 보내도록 함
    return redirect('articles:index')

def edit(request, article_pk):
    """
    [수정 페이지 제공]
    """
    # 1. 수정하고자 하는 대상을 조회
    article = Article.objects.get(pk=article_pk)

    # 2. 수정 대상 객체를 context에 담아
    context = {
        'article': article,
    }

    # 3. 수정 edit 페이지를 렌더링
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    """
    [실제로 DB에 데이터를 수정 진행]
    """
    # 1. 몇 번 게시글을 수정하는지 조회
    article = Article.objects.get(pk=article_pk)

    # 2. 조회한 게시글의 인스턴스 변수를 갱신
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    # 3. 저장(갱신)
    article.save()

    # 4. 수정한 게시글의 상세 페이지로 요청을 보낼 수 있도록 redirect
    return redirect('articles:detail', article.pk)