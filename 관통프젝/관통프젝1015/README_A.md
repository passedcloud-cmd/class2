# 03-pjt : 반응형 웹 페이지 구성

AI 기반 도서 분석 및 창작 지원 통합 솔루션 서비스 ThRead의 메인 페이지를 HTML, CSS, Bootstrap 5.3으로 만든 프로젝트

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 목표 | Bootstrap 컴포넌트와 Grid System으로 반응형 레이아웃 구성하기 |
| 사용 기술 | HTML, CSS, Bootstrap 5.3 |
| 개발 도구 | Visual Studio Code, Google Chrome, GitLab |

## 단계별 구현 과정

### 1. Navbar & Hero (F301, F302) - `01-navbar.html`

#### 구현한 내용
- 로고 "ThRead"의 `Th`는 흰색, `Read`는 붉은색(#fe4a51)으로 표시
- 메뉴(쓰레드, 도서 검색, 마이 페이지, 로그아웃)는 흰색이고, 마우스를 올리면 붉은색으로 바뀜
- 화면 폭이 576px 미만이면 햄버거 버튼(토글)으로 바뀜
- Navbar를 `position: absolute`로 Hero 이미지 위에 띄움
- 모바일에서는 Hero 제목이 "AI 기반 도서 분석 및" 뒤에서 줄바꿈됨

#### 학습한 내용
한 단어 안에서 색 나누기: `<span>`으로 감싸서 따로 색을 줄 수 있었다.

```html
<a class="navbar-brand" href="#">
  <span class="th">Th</span><span class="read">Read</span>
</a>
```

반응형 Navbar: `navbar-expand-sm`의 `sm`은 576px을 뜻한다. 576px 이상에서는 메뉴가 펼쳐지고, 그보다 작으면 접혀서 햄버거 버튼이 된다. 처음에는 직접 미디어 쿼리를 써야 하는 줄 알았는데, class 하나로 해결되어서 신기했다.

화면 크기에 따라 줄바꿈하기: `<br>` 태그에도 class를 붙일 수 있다는 걸 처음 알았다. `d-sm-none`은 576px 이상에서 `display: none`이 되므로, 모바일에서만 줄바꿈이 된다.

```html
AI 기반 도서 분석 및<br class="d-sm-none" />
창작 지원 통합 솔루션 서비스
```

#### 어려웠던 부분
- 햄버거 아이콘이 안 보였다. 배경이 투명하다 보니 기본 검은색 아이콘이 어두운 사진 위에서 잘 보이지 않았다. `data-bs-theme="dark"`를 붙이니 아이콘이 흰색으로 바뀌었다.
- 폰트가 적용되지 않았다. 처음 받은 코드에는 `format("ttf")`로 적혀 있었는데, 브라우저는 이 값을 인식하지 못한다. `format("truetype")`으로 고치고 나서야 폰트가 적용됐다. 개발자 도구(F12)의 Network 탭을 보고 폰트 파일이 아예 로드되지 않는다는 걸 확인할 수 있었다. 스켈레톤 파일 5개에 모두 같은 문제가 있어서, 팀원 B에게도 바로 알려 04, 05 파일도 함께 고쳤다.
- 모바일에서 한글이 글자 단위로 끊겼다. 모바일에서 Hero 제목의 "서비스"가 "서비"와 "스"로 나뉘어 줄바꿈되었다. 576px 미만에서 글자 크기를 조금 줄이고, `word-break: keep-all`을 넣어 한글도 단어 단위로 줄바꿈되게 고쳤다.

### 2. 베스트셀러 (F303) - `02-bestseller.html`

#### 구현한 내용
- 12권을 4권씩 묶어 슬라이드 3장으로 구성하고, 3초마다 자동으로 넘어가게 함
- 왼쪽에는 "베스트셀러" 제목, 오른쪽에는 Carousel 배치
- 모든 표지 이미지를 너비 150px, 높이 220px로 고정
- Next 버튼만 오른쪽에 두고, 붉은 원형으로 꾸밈

#### 학습한 내용
Carousel 구조: `.carousel` → `.carousel-inner` → `.carousel-item` 순서로 감싸야 한다. 첫 번째 슬라이드에는 반드시 `active`를 붙여야 한다는 것도 알게 되었다. 처음에 `active`를 빼먹었더니 화면에 아무것도 나오지 않았다.

자동 전환: `data-bs-ride="carousel"`만 넣으면 JavaScript를 직접 쓰지 않아도 자동으로 슬라이드가 넘어간다. `data-bs-interval="3000"`으로 넘어가는 간격(3초)을 정할 수 있다.

Next 버튼만 남기기: 공식 문서 예제의 Prev 버튼(`carousel-control-prev`)을 지우기만 하면 됐다.

이미지 크기 고정: 이미지 크기를 강제로 맞추면 사진이 찌그러진다. `object-fit: cover`를 쓰면 비율은 유지하고 넘치는 부분만 잘린다.

```css
.book-cover {
  width: 150px;
  height: 220px;
  object-fit: cover;
}
```

#### 어려웠던 부분
- 슬라이드 하나에 책 4권 넣기. Carousel은 보통 사진 한 장씩 넘기는 예제만 있어서 헷갈렸다. `carousel-item` 안에 `row`를 만들고, 그 안에 `col-md-3` 4개를 넣는 방식으로 해결했다.
- Next 버튼 위치. 기본 Next 버튼은 Carousel 높이 전체를 덮는 투명한 영역이다. 예시처럼 동그란 버튼으로 만들려고 `width`, `height`, `border-radius: 50%`, `top`을 직접 지정했다.
- 모바일에서 책 4권이 한 줄에 다 들어가지 않았다. 150px × 4권에 간격까지 더하면 600px이 넘는다. 모바일에서는 `col-6`으로 두 권씩 두 줄이 되도록 바꿨다.

### 3. AI 추천 (F304) - `03-ai_recommendation.html`

#### 구현한 내용
- 섹션 폭 80%, 가운데 정렬
- 왼쪽(도서 이미지 3개)과 오른쪽(소개 텍스트)의 비율을 7:5로 나누고, 세로 가운데 정렬
- 활동 데이터 기반을 강조 (#fe4a51, SBAggroOTF_L 폰트, 1.3rem)

#### 학습한 내용
Bootstrap Grid System: 한 줄을 12칸으로 나누어 쓴다. 7:5는 `col-md-7`과 `col-md-5`로 만들면 된다(7 + 5 = 12). `md`가 붙어 있으므로 768px 미만에서는 두 영역이 위아래로 쌓인다.

```html
<div class="ai-recommendation row align-items-center">
  <div class="col-12 col-md-7">이미지 3개</div>
  <div class="col-12 col-md-5">소개 텍스트</div>
</div>
```

세로 가운데 정렬: `row`는 내부적으로 `display: flex`이기 때문에, 수업에서 배운 `align-items: center`(Bootstrap class로는 `align-items-center`)가 그대로 적용된다. Grid System도 결국 Flexbox로 만들어졌다는 걸 알게 되었다.

문장 일부만 강조하기: 문장 중 일부만 `<span class="highlight">`로 감싸서 스타일을 줬다.

#### 어려웠던 부분
- `row` class를 붙이면 Bootstrap이 좌우에 음수 margin을 넣는다. 그래서 `margin: 0 auto`로 가운데 정렬한 것이 깨질까 봐 걱정했다. 확인해 보니 내 `<style>`이 Bootstrap CSS보다 나중에 불러와져서 내 스타일이 적용됐다. 명시도가 같으면 나중에 작성된 CSS가 이긴다는 규칙을 직접 확인할 수 있었다.

## 새로 배운 것 정리

| 개념 | 한 줄 정리 |
|---|---|
| Bootstrap Breakpoint | `sm`=576px, `md`=768px, `lg`=992px. class에 붙이면 "이 크기 이상부터" 적용 |
| Grid System | 한 줄 = 12칸. `col-7` + `col-5` = 7:5 비율 |
| 모바일 퍼스트 | 기본값은 모바일 기준, 큰 화면 설정은 `col-sm-*`, `col-md-*`로 덧붙임 |
| Carousel | `carousel-inner` > `carousel-item`, 첫 슬라이드에 `active` 필수 |
| `object-fit: cover` | 이미지 비율을 지키면서 지정된 크기를 꽉 채움 |
| CSS 우선순위 | 명시도가 같으면 나중에 쓴 CSS가 이김 |
| `data-bs-*` 속성 | JS를 직접 쓰지 않아도 Carousel, 토글이 동작 |
| `@font-face` | 폰트 파일을 직접 불러와서 이름을 붙여 사용. `format` 값을 정확히 써야 함 |
| `word-break: keep-all` | 한글이 글자 단위가 아니라 단어 단위로 줄바꿈됨 |

## 문제 해결에 도움이 된 방법

1. 개발자 도구(F12): 요소를 클릭하면 어떤 CSS가 적용되었고, 어떤 CSS가 줄 그어져서 무시되었는지 바로 보인다. 폰트 문제를 찾을 때는 Network 탭이 큰 도움이 되었다.
2. 디바이스 툴바(Ctrl + Shift + M): 화면 폭을 바꿔 가며 576px 전후로 레이아웃이 바뀌는지 확인했다.
3. Bootstrap 공식 문서: 컴포넌트마다 예제 코드가 있어서 복사한 뒤 필요한 부분만 고치는 방식으로 작업했다.
4. 생성형 AI: 막히는 부분(Carousel 한 슬라이드에 여러 장 넣기, 폰트가 안 나오는 원인 등)을 질문해서 방향을 잡았다. 받은 코드는 그대로 쓰지 않고, 개발자 도구로 확인하며 이해한 뒤 적용하려고 노력했다.
5. 팀원과의 교차 확인: 서로의 화면을 모바일 크기로 확인해 주면서, 혼자서는 놓쳤던 문제를 찾을 수 있었다.

## 느낀 점

스켈레톤 코드에서 `display: flex`를 `d-flex`처럼 적는 등 수업에서 배운 것과 다르게 표기하여 처음에는 헷갈렸으나 비슷한 코드가 반복되니 class 이름만 보고 어느 정도 뜻을 짐작할 수 있게 되었다.

폰트가 안 나왔던 문제에서 가장 많은 시간을 소모했다. 코드를 계속 들여다볼 때는 원인을 몰랐고, 개발자 도구로 폰트 파일이 아예 불러와지지 않는다는 걸 확인하고 나서야 `format` 값 하나가 문제라는 걸 찾았다. 앞으로는 막히면 코드만 보지 말고 개발자 도구부터 열어 봐야겠다.

협업 측면에서는 시작 전에 색상, 제목 스타일, 섹션 폭을 미리 맞춰 둔 것이 가장 잘한 일이었다. 각자 따로 작업했는데도 06에서 합쳤을 때 한 사이트처럼 보였다. 앞으로도 작업 시작 전에 스타일 요소를 통일해야겠다.
