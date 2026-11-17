# REST API 예시 문제

Django REST Framework 기반의 게시글(Article) REST API 디버깅 예시 문제입니다.
스켈레톤 코드에는 오류가 포함되어 있습니다. 문제지의 [현재 증상]을 Postman으로 직접 확인하고,
명시된 수정 파일의 코드를 고쳐 [정상 동작]이 되도록 디버깅합니다.

---

## 프로젝트 실행 방법

### 1. 가상환경 생성 및 패키지 설치

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

### 2. 개발 서버 실행

주어진 `db.sqlite3` 에 테이블과 데이터가 들어 있으므로 migrate 는 필요하지 않습니다.

```bash
python manage.py runserver
```

서버가 실행되면 `http://127.0.0.1:8000/` 에서 API를 사용할 수 있습니다.

---

## 전체 API 엔드포인트 목록

모든 URL은 `/api/v1/` 로 시작하며, **끝에 `/` 를 붙여** 요청합니다.

| Method | URL | 설명 |
|--------|-----|------|
| GET | `/api/v1/articles/` | 게시글 목록 조회 |
| POST | `/api/v1/articles/` | 게시글 생성 |
| GET | `/api/v1/articles/<article_pk>/` | 게시글 상세 조회 |
| PUT | `/api/v1/articles/<article_pk>/` | 게시글 수정 |
| DELETE | `/api/v1/articles/<article_pk>/` | 게시글 삭제 |

---

## 모델 구조

| 모델 | 필드 |
|------|------|
| Article | id, title(제목), content(내용), created_at, updated_at |

- `models.py` 는 수정하지 않습니다.

## 프로젝트 구조

```
REST API 예시 문제 Code/
├── config/               # 프로젝트 설정 (settings.py, urls.py)
├── articles/
│   ├── models.py         # Article 모델
│   ├── serializers.py    # 직렬화 클래스
│   ├── urls.py           # articles 앱 URL
│   └── views.py          # API view 함수
├── db.sqlite3            # 데이터가 들어 있는 DB
├── problem_05.md         # 서술형 답안 작성 파일
├── answer.md             # 예시 문제 답안 및 해설
├── manage.py
└── requirements.txt
```
