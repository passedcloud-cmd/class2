# REST API 예시 문제 - 답안 및 해설

> 평가 준비용 해설입니다. 먼저 직접 풀어 본 뒤 확인하세요.
> 실제 평가도 같은 방식으로 진행됩니다. 문제지의 **[현재 증상]**을 Postman으로 직접 재현하고, **수정 파일**에서 원인을 찾아 **[정상 동작]**이 되도록 고칩니다.

---

## 디버깅 접근 방법

1. **증상 재현**: 문제의 Request를 Postman으로 그대로 보내 응답 상태 코드와 응답 본문을 확인합니다.
2. **에러 메시지 읽기**: 500 오류라면 `runserver`를 실행한 터미널의 Traceback 마지막 줄부터 읽습니다. 어떤 예외가 어느 파일의 몇 번째 줄에서 났는지가 적혀 있습니다.
3. **요청 흐름 따라가기**: URL(`urls.py`) → view 함수(`views.py`) → serializer(`serializers.py`) 순서로 따라가며, 요청 Method에 해당하는 분기만 집중해서 봅니다.
4. **정상 코드와 비교**: 같은 파일의 다른 분기 코드나 수업 실습 코드와 비교하면 빠진 부분이 잘 보입니다.
5. **수정 후 재확인**: 고친 뒤 같은 요청을 다시 보내 [정상 동작]대로 응답하는지 확인하고, 다른 요청이 깨지지 않았는지도 확인합니다.

---

## 문제 01. 게시글 상세 조회 응답 필드 누락 디버깅

- Request : `GET /api/v1/articles/<int:article_pk>/`
- 수정 파일 : `articles/views.py`

### 원인

상세 조회(GET) 분기에서 목록용 serializer인 `ArticleListSerializer`를 사용하고 있습니다.
`ArticleListSerializer`는 `fields = ('id', 'title',)`이므로 두 필드만 응답됩니다.

### 수정

```python
# 수정 전
if request.method == 'GET':
    serializer = ArticleListSerializer(article)

# 수정 후
if request.method == 'GET':
    serializer = ArticleSerializer(article)
```

### 핵심 개념

- 응답에 어떤 필드가 담길지는 **어떤 serializer를 쓰는지**, 그리고 그 serializer의 `Meta.fields`가 결정합니다.
- 목록은 간단한 정보만, 상세는 모든 정보를 보여주도록 serializer를 나눠 쓰는 경우가 많습니다. 응답 필드가 이상하면 view가 고른 serializer와 `fields`를 함께 확인합니다.

---

## 문제 02. 게시글 생성 500 오류 디버깅

- Request : `POST /api/v1/articles/`
- 수정 파일 : `articles/views.py`

### 원인

사용자가 보낸 데이터를 `data=` 키워드 없이 첫 번째 인자로 넘기고 있습니다.
serializer의 첫 번째 위치 인자는 `instance`(기존 객체)이므로, `request.data`가 instance로 들어갑니다.
`data=` 없이 만든 serializer에서 `is_valid()`를 호출하면 DRF가 `AssertionError`를 발생시켜 500이 됩니다.

터미널 Traceback 예시:

```
AssertionError: Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
```

### 수정

```python
# 수정 전
serializer = ArticleSerializer(request.data)

# 수정 후
serializer = ArticleSerializer(data=request.data)
```

### 핵심 개념

- 사용자 입력으로 **생성**할 때는 `Serializer(data=request.data)` 형태로 넘기고, `is_valid()`로 유효성 검사를 한 뒤 `save()`합니다.
- 500 오류는 Postman 응답보다 **서버 터미널의 Traceback**에 원인이 더 정확히 적혀 있습니다.

---

## 문제 03. 게시글 수정 오류 디버깅

- Request : `PUT /api/v1/articles/<int:article_pk>/`
- 수정 파일 : `articles/views.py`

### 원인

수정(PUT) 분기에서 serializer에 **수정할 기존 게시글(`article`)을 넘기지 않았습니다.**
instance 없이 `data`만 넘기면 `save()`가 내부적으로 `create()`를 호출해 새 게시글을 만듭니다.
그래서 200 OK가 오지만 기존 게시글은 그대로이고 새 글이 하나 더 생깁니다.

### 수정

```python
# 수정 전
serializer = ArticleSerializer(data=request.data)

# 수정 후
serializer = ArticleSerializer(article, data=request.data)
```

### 핵심 개념

- `save()`는 instance가 **없으면 `create()`**, **있으면 `update()`**를 호출합니다.
- 수정 요청에서는 반드시 `Serializer(기존객체, data=request.data)` 형태로 기존 객체와 새 데이터를 함께 넘깁니다.
- 증상이 "에러는 없는데 결과가 이상하다"일 때는 응답 코드만 보지 말고, 목록 조회 등으로 **DB 상태를 다시 확인**하는 습관이 중요합니다.

---

## 문제 04. 게시글 삭제 오류 디버깅

- Request : `DELETE /api/v1/articles/<int:article_pk>/`
- 수정 파일 : `articles/views.py`

### 원인

DELETE 분기에서 204 응답만 보내고, 게시글을 실제로 삭제하는 `article.delete()`가 없습니다.

### 수정

```python
# 수정 전
elif request.method == 'DELETE':
    return Response(status=status.HTTP_204_NO_CONTENT)

# 수정 후
elif request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

### 핵심 개념

- 상태 코드는 view가 **직접 정해서 보내는 값**일 뿐, 실제 작업이 성공했다는 보장이 아닙니다.
- 삭제 후에는 같은 게시글을 다시 조회해 정말 없어졌는지 확인합니다.

---

## 문제 05. [서술형] 직렬화(Serialization)

### 예시 답안

직렬화(Serialization)란 Django의 모델 객체나 QuerySet 같은 **복잡한 데이터를, 저장하거나 전송할 수 있는 형식(예: JSON)으로 변환하는 과정**이다.
DRF에서는 Serializer가 모델 인스턴스를 Python 기본 데이터 타입으로 변환하고, 이것이 JSON으로 렌더링되어 클라이언트에 응답된다.

### 작성 포인트

- **무엇을** → 객체·QuerySet 등 복잡한 데이터를
- **어떻게** → 저장·전송 가능한 형식(JSON 등)으로 **변환하는 것**
- 개념과 다른 설명(예: "데이터베이스에 저장하는 것", "데이터를 암호화하는 것")이 섞이면 오답이 될 수 있으니, 확실한 내용만 정확하게 작성합니다.

---

## 최종 정답 코드 (`articles/views.py`)

```python
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # 문제 02: 사용자 입력은 data= 키워드로 전달
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        # 문제 01: 상세 조회는 모든 필드를 가진 ArticleSerializer 사용
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 문제 03: 수정할 기존 게시글(article)을 함께 전달
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # 문제 04: 실제로 삭제한 뒤 204 응답
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
