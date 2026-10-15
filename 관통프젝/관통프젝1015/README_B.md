# 03-pjt : 반응형 웹 페이지 구성

> AI 기반 도서 분석 및 창작 지원 통합 솔루션 서비스 ThRead의 메인 페이지를 HTML, CSS, Bootstrap 5.3으로 만든 프로젝트

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 목표 | Bootstrap 컴포넌트와 Grid System으로 반응형 레이아웃 구성하기 |
| 사용 기술 | HTML, CSS, Bootstrap 5.3 |
| 개발 도구 | Visual Studio Code, Google Chrome, GitLab |
| 개발 기간 | 2026년 10월 15일 하루 |

### 파일 구조

```
03-pjt/
├── 01-navbar.html            #  F301, F302 Navbar & Hero
├── 02-bestseller.html        #  F303 베스트셀러 (Carousel)
├── 03-ai_recommendation.html #  F304 AI 추천 (Grid System)
├── 04-genre_list.html        #  F305 장르별 도서 목록 (Flexbox)
├── 05-popular_thread.html    #  F306 인기 쓰레드 (Card, Pagination)
├── 06-main.html              #  F307 메인 페이지 결합 + F308 로그아웃 Modal
├── assets/                   # 이미지, 폰트
└── README.md
```

## 단계별 구현 과정

### 1. 장르별 도서 목록 (F305) - `04-genre_list.html`

#### 구현한 내용
- 섹션 폭 80%, 가운데 정렬
- Flexbox로 장르 10개를 4열로 배치하고, 576px 미만에서는 1열로 배치
- 이미지 왼쪽 아래에 장르명을 겹쳐서 표시 (오버레이)
- 아이템 높이를 200px로 고정하고, 이미지가 아이템을 꽉 채우도록 함

#### 학습한 내용
Flexbox로 4열 만들기: `flex-wrap: wrap`으로 줄바꿈을 허용하고, 아이템 하나의 폭을 4분의 1로 지정했다. 이때 아이템 사이 간격(`gap`) 3개만큼을 빼야 정확히 4개가 한 줄에 들어간다. `calc()`라는 CSS 계산 함수를 처음 써봤다.

```css
.genre-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.genre-item {
  flex: 0 0 calc((100% - 3rem) / 4); /* gap 1rem × 3개 */
  height: 200px;
}
```

글자를 이미지 위에 겹치기: 부모에 `position: relative`, 글자에 `position: absolute`를 주면 글자가 부모를 기준으로 배치된다. 수업에서 배운 position 개념을 실제로 써본 첫 경험이었다.

```css
.genre-item { position: relative; }
.genre-name {
  position: absolute;
  left: 0.75rem;
  bottom: 0.5rem;
}
```

이미지를 부모 크기에 맞추기: `width: 100%; height: 100%`만 주면 사진이 찌그러진다. `object-fit: cover`를 함께 쓰면 비율을 유지한 채 꽉 채우고, 넘치는 부분은 잘린다.

미디어 쿼리: `max-width: 575.98px`는 "576px 미만"이라는 뜻이다. Bootstrap도 같은 값을 쓴다. 576px로 쓰면 정확히 576px일 때도 모바일 스타일이 적용되어 버리기 때문이다.

```css
@media (max-width: 575.98px) {
  .genre-item {
    flex: 0 0 100%;
  }
}
```

#### 어려웠던 부분
- 처음에는 `width: 25%`로 했더니 `gap` 때문에 4번째 아이템이 다음 줄로 밀려났다. 개발자 도구로 박스 크기를 확인하고 나서야 간격까지 계산해야 한다는 걸 알았다.
- 사진 위의 흰 글씨가 밝은 사진에서는 잘 보이지 않아서 `text-shadow`로 그림자를 넣었다.
- 마우스를 올렸을 때 이미지가 살짝 커지게 하려고 `transform: scale(1.05)`를 넣었다. 그랬더니 이미지가 아이템 밖으로 튀어나왔다. 부모에 `overflow: hidden`을 줘서 해결했다.

### 2. 인기 쓰레드 (F306) - `05-popular_thread.html`

#### 구현한 내용
- Card 컴포넌트로 쓰레드 6개 출력 (데스크탑 3열, 576px 미만 1열)
- 카드 이미지 높이를 200px로 고정
- 저자와 도서명은 항상 카드 맨 아래에 표시하고, 도서명은 #fe4a51
- Pagination은 테두리를 없애고 배경을 투명하게 했으며, 현재 페이지 번호는 #fe4a51

#### 학습한 내용
카드 반응형 배치: `col-12 col-sm-4`는 "기본은 12칸(1열), 576px 이상이면 4칸(3열)"이라는 뜻이다. Bootstrap은 작은 화면을 먼저 생각하고(모바일 퍼스트) 큰 화면 설정을 덧붙이는 방식이라는 걸 이해했다.

카드 높이 맞추기 + 하단 고정: 카드마다 본문 길이가 달라서 높이가 들쭉날쭉했다. 카드에 `h-100`(height: 100%)을 주니 같은 줄의 카드 높이가 같아졌다. 저자/도서명을 `card-footer`에 넣으면 항상 카드 맨 아래에 붙는다.

CSS 명시도(Specificity): 이번 과제에서 가장 크게 배운 부분이다. Bootstrap의 `.page-link`보다 내 스타일이 이기게 하려고 선택자를 더 구체적으로 썼다.

```css
/* class 4개 → Bootstrap의 .page-link(class 1개)보다 명시도가 높음 */
.thread .pagination .page-item .page-link {
  border: none;
  background-color: transparent;
}
.thread .pagination .page-item.active .page-link {
  color: #fe4a51;
}
```

#### 어려웠던 부분
- 처음에는 `.page-link { border: none; }`만 썼는데 활성화된 페이지는 여전히 파란 배경이었다. Bootstrap이 `.active > .page-link`처럼 더 구체적인 선택자로 스타일을 주고 있었기 때문이다. `!important`를 쓰면 쉽게 해결되겠지만, 요구사항이 "명시도를 높여서"였기 때문에 선택자를 길게 쓰는 방법으로 해결했다.
- 본문 요약이 길면 카드가 너무 길어졌다. 검색해 보니 `-webkit-line-clamp`로 3줄까지만 보여주고 나머지는 "..."으로 줄일 수 있었다.
- `.container`는 Bootstrap이 화면 크기별로 `max-width`를 정해 둬서 `width: 80%`만으로는 폭이 바뀌지 않았다. `max-width: 80%`도 함께 지정해야 했다.

### 3. 메인 페이지 결합 (F307) - `06-main.html`

#### 구현한 내용
- 01~05의 섹션을 순서대로 한 파일에 합침
- 다섯 파일의 `<style>`을 하나로 정리

#### 어려웠던 부분
- 같은 class 이름이 충돌했다. `.section-title`은 이름만 미리 맞췄을 뿐, 파일마다 세부 스타일이 조금씩 달랐다. 03번은 margin 0, 04번은 가운데 정렬에 아래 여백 2rem이었다. 그대로 합치면 마지막에 쓴 스타일이 앞의 것을 덮어써서 다른 섹션까지 바뀌었다. 그래서 공통 스타일은 하나만 남기고, 섹션마다 다른 부분은 `.genre-books .section-title`처럼 부모 class를 앞에 붙여서 그 섹션에서만 적용되게 했다.

  ```css
  /* 공통 */
  .section-title { font-family: "GmarketSansTTFMedium"; font-size: 1.4rem; margin: 0; }
  /* 장르 섹션에서만 */
  .genre-books .section-title { text-align: center; margin-bottom: 2rem; }
  ```
- 결합하고 나서야 보인 문제. 합친 페이지를 모바일 크기로 확인하다가 Hero 제목의 "서비스"가 "서비"와 "스"로 나뉘어 줄바꿈되는 것을 발견했다. 01 파일에서 `word-break: keep-all`로 고쳤고, 06에도 같은 수정을 반영했다.

#### 배운 점
파일을 나눠서 작업할 때는 문제가 없어도, 합치는 순간 CSS 충돌이 생길 수 있다. 처음부터 class 이름을 섹션별로 구분해 두면 결합할 때 훨씬 편하겠다고 느꼈다.

### 4. 로그아웃 확인 Modal (F308) - `06-main.html`

#### 구현한 내용
- Navbar의 "로그아웃"을 누르면 확인 창이 화면 가운데에 뜸
- 오른쪽 위에 닫기(X) 버튼
- "정말 로그아웃 하시겠습니까?"를 가운데 정렬로 표시하고, 취소/로그아웃 버튼 배치
- X 버튼, 취소, 로그아웃, 창 바깥 클릭 중 무엇을 해도 Modal이 닫힘

#### 학습한 내용
JavaScript 없이 Modal 열고 닫기:
- 여는 쪽: `data-bs-toggle="modal"`과 `data-bs-target="#logoutModal"`(Modal의 id)을 링크에 붙이면 된다. Navbar의 로그아웃 링크에 이 두 속성만 추가했다.
- 닫는 쪽: 버튼에 `data-bs-dismiss="modal"`을 붙이면 클릭할 때 닫힌다.
- 창 바깥을 클릭하면 닫히는 기능은 Bootstrap에 기본으로 들어 있었다.

```html
<a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#logoutModal">로그아웃</a>

<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
```

`modal-dialog-centered`를 추가하면 Modal이 화면 세로 가운데에 나타난다.

#### 어려웠던 부분
- Bootstrap의 JS 파일(`bootstrap.bundle.min.js`)이 없으면 Modal, Carousel, 햄버거 메뉴가 전부 동작하지 않는다. 이 기능들은 CSS만으로 되는 게 아니라 JS가 필요한 컴포넌트라는 걸 알게 되었다.
- 로그아웃 버튼 색을 `#fe4a51`로 바꾸려고 `.btn-danger`를 썼더니 Bootstrap 기본 빨간색이 나와서 색이 미묘하게 달랐다. 직접 `.btn-logout` class를 만들어 색을 지정했다.

## 새로 배운 것 정리

| 개념 | 한 줄 정리 |
|---|---|
| Flexbox 줄바꿈 | `flex-wrap: wrap` + 아이템 폭 지정으로 여러 열 배치 |
| `calc()` | `calc((100% - 3rem) / 4)`처럼 CSS 안에서 계산 |
| `position: relative` / `absolute` | 부모를 기준으로 자식을 원하는 위치에 겹쳐 놓기 |
| `object-fit: cover` | 이미지 비율을 지키면서 지정된 크기를 꽉 채움 |
| 미디어 쿼리 | `max-width: 575.98px` = 576px 미만 |
| 모바일 퍼스트 | 기본값은 모바일 기준, 큰 화면 설정은 `col-sm-*`로 덧붙임 |
| CSS 명시도 | 선택자가 구체적일수록 우선. 같으면 나중에 쓴 CSS가 이김 |
| 부모 선택자로 범위 좁히기 | `.genre-books .section-title`처럼 특정 섹션에만 스타일 적용 |
| `data-bs-*` 속성 | JS를 직접 쓰지 않아도 Modal이 열리고 닫힘 |

## 문제 해결에 도움이 된 방법

1. 개발자 도구(F12): 요소를 클릭하면 어떤 CSS가 적용되었고, 어떤 CSS가 줄 그어져서 무시되었는지 바로 보인다. 명시도 문제와 결합 시 스타일 충돌을 해결할 때 가장 큰 도움이 되었다.
2. 디바이스 툴바(Ctrl + Shift + M): 화면 폭을 바꿔 가며 576px 전후로 레이아웃이 바뀌는지 확인했다.
3. Bootstrap 공식 문서: Card, Pagination, Modal 예제 코드를 복사한 뒤 필요한 부분만 고치는 방식으로 작업했다.
4. 생성형 AI: 막히는 부분(gap을 포함한 폭 계산, 줄 수 제한 방법 등)을 질문해서 방향을 잡았다. 받은 코드는 그대로 쓰지 않고, 개발자 도구로 확인하며 이해한 뒤 적용하려고 노력했다.
5. 팀원과의 교차 확인: 결합 후 화면을 함께 확인하면서, 각자 파일에서는 보이지 않던 문제를 찾을 수 있었다.

## 느낀 점

처음 Bootstrap을 접했을 때는 class 이름이 너무 많아서 막막했다. 그런데 04번 장르 목록은 Bootstrap 없이 수업에서 배운 Flexbox와 position만으로 만들 수 있었다. 배운 개념이 실제 화면으로 나오는 걸 보니 뿌듯했다. 반대로 05번에서 Bootstrap 컴포넌트를 쓰면서는 "편하지만, 내 마음대로 바꾸려면 Bootstrap이 어떤 CSS를 넣고 있는지 알아야 한다"는 걸 느꼈다. Pagination 색이 안 바뀌어서 한참 헤맨 경험 덕분에 명시도 개념이 확실히 머리에 남았다.

가장 많이 배운 건 06 결합 작업이었다. 각자 파일에서는 완벽해 보였는데, 합치는 순간 `.section-title`이 서로 덮어쓰면서 레이아웃이 틀어졌다. 시작 전에 색상이나 폰트 같은 규칙을 맞춰 둔 덕분에 충돌이 적은 편이었지만, 세부 스타일까지 미리 정하거나 class 이름을 섹션별로 구분했다면 더 수월했을 것이다. 다음 협업에서는 공통 CSS 파일을 따로 만들어 함께 쓰는 방식을 제안해 보고 싶다.