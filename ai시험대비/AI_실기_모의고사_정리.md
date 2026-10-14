# 🧪 AI 코딩 실습 평가 — 모의고사 분석 & 대비 정리

> **모의고사:** 와인 성분 13개로 품종(0/1/2) 분류 · 8문항 100점 · 120분
> 아래 답안 코드는 같은 원천 데이터(scikit-learn wine)로 **직접 실행해서 확인**했어.

---

## 0. 시험 형식부터 파악하기

| 특징 | 의미 | 대처 |
|---|---|---|
| `실행만 하세요` / `작성하세요` 셀 | 빈칸(`None`) 채우기 형식 | **지정된 변수 이름·반환 형식 그대로** 유지 |
| 문항마다 데이터를 따로 제공 | 앞 문항을 못 풀어도 다음 문항 가능 | 막히면 **바로 다음 문항으로** |
| 정확도 목표 없음 | 성능이 아니라 **과정**을 채점 | 시키는 옵션(`random_state`, `lr`, `p` 등)을 **정확히** |
| 확인 셀 | 내 답이 맞는 형태인지 보여줌 | 작성 후 **꼭 실행**해서 shape·출력 확인 |
| 제출 = 실행 결과가 남은 노트북 | 실행 안 한 셀은 결과가 없음 | 마지막에 **위에서부터 전체 실행** |

**배점 흐름:** 데이터 다루기(1~2번, 22점) → 머신러닝(3~4번, 26점) → 딥러닝(5~8번, 52점)
👉 **딥러닝(PyTorch)이 절반 이상**이야. 특히 6번(학습 루프, 18점)이 제일 커.

---

## 1. 품종 비율을 유지하며 데이터 나누기 [12점]

### 개념
- **stratify(층화 분할):** 학습용·검증용에 **클래스 비율을 똑같이** 유지해서 나누는 것
  - 안 하면 어떤 품종이 한쪽에 몰려서 평가가 왜곡될 수 있어
- `value_counts()`는 **개수가 많은 순**으로 정렬돼 → 번호 순으로 보려면 `.sort_index()`

### 답안
```python
# (a) 품종별 개수 (0, 1, 2 순서)
counts = dev['label'].value_counts().sort_index()

# (b) 75:25 층화 분할
train_df, valid_df = train_test_split(
    dev,
    test_size=0.25,
    random_state=23,
    stratify=dev['label'],     # ★ 정답 열을 넘김
)
```

### ⚠️ 함정
- `.sort_index()` 빠뜨리면 순서가 개수순이라 틀려
- DataFrame을 통째로 넣으면 **모든 열과 원래 인덱스가 유지**돼 (문제 조건 충족). `reset_index()` 하지 마
- 반환 순서: DataFrame 하나 넣으면 `train, valid` 2개 / `X, y` 두 개 넣으면 `X_train, X_test, y_train, y_test` 4개

---

## 2. 학습 자료의 분포 확인하기 [10점]

### 개념
- **groupby:** 같은 값끼리 묶어서 통계 계산 → "품종별 평균"
- 결과 인덱스는 자동으로 **오름차순(0, 1, 2)** 정렬돼
- 산점도에서 `c=`에 라벨을 넣으면 **라벨마다 색이 달라져**

### 답안
```python
# (a) 품종별 두 측정값의 평균 (열 순서 지키기)
group_mean = stats_df.groupby('label')[['alcohol', 'color_intensity']].mean()

# (b) 산점도: x=alcohol, y=color_intensity, 색=label
ax.scatter(stats_df['alcohol'], stats_df['color_intensity'], c=stats_df['label'])
```

**범례까지 넣고 싶으면 (이것도 정답)**
```python
for k, g in stats_df.groupby('label'):
    ax.scatter(g['alcohol'], g['color_intensity'], label=f'class {k}')
ax.legend()
```

### ⚠️ 함정
- 열 두 개 선택은 **대괄호 두 번** `[['a', 'b']]` (한 번이면 에러)
- `ax.scatter`로 그려야 해. `plt.subplots`를 또 만들면 제공된 `ax`가 비어 버려
- "품종 번호를 측정값에 합치지 마라" → `label`은 **색(c)에만** 쓰기

### 같이 알아둘 pandas
```python
df.shape / df.info() / df.describe()        # 크기, 타입, 통계
df.isnull().sum()                           # 결측치 개수
df['col'].mean() / .std() / .min() / .max()
df.groupby('label').size()                  # 그룹별 개수 (value_counts와 비슷)
df.corr(numeric_only=True)                  # 상관계수
df[df['label'] == 1]                        # 조건으로 행 고르기
```

---

## 3. kNN 분류기 학습하기 [12점]

### 개념
- **kNN:** 새 시료와 **가장 가까운 k개 학습 시료**를 찾아 다수결로 품종 결정
- **거리 기반**이라서 표준화가 중요해 (이번엔 준비 코드가 이미 해 줌)
- 싸이킷런 공통 3단계: **생성 → `fit` → `predict`**

### 답안
```python
# (a) 생성 + 학습
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# (b) 검증 시료 예측
pred = knn.predict(X_valid)        # 길이 36 배열
```

### ⚠️ 함정
- `knn = KNeighborsClassifier(...).fit(...)`로 한 줄에 써도 돼 (`fit`이 모델 자신을 반환)
- **검증 데이터로 `fit` 하면 안 돼** (문제에서도 금지)

### 다른 모델이 나와도 똑같아
```python
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
model = LogisticRegression(max_iter=1000); model.fit(X_train, y_train)
model.predict(X_valid)            # 클래스
model.predict_proba(X_valid)      # 클래스별 확률 (n, 클래스 수)
```

### 표준화를 직접 하라고 하면
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)   # ★ 학습용으로만 fit
X_valid_s = scaler.transform(X_valid)       # 검증·테스트는 transform만
```

---

## 4. 정확도와 혼동행렬 [14점]

### 개념
- **정확도** = 맞힌 개수 / 전체 (비율 0~1)
- **혼동행렬** (싸이킷런 기준): **행 = 실제**, **열 = 예측**
  - 대각선 `cm[i, i]` = 맞힌 개수
  - `cm[i, j]` (i≠j) = 실제 i를 j로 잘못 예측
- **실제 품종 1인데 틀린 개수** = 1행 전체 합 − 대각선 = `cm[1].sum() - cm[1, 1]`

### 답안
```python
# (a) 정확도 (비율)
acc = accuracy_score(actual, guessed)
# 같은 뜻: acc = (actual == guessed).mean()

# (b) 3×3 혼동행렬
cm = confusion_matrix(actual, guessed, labels=[0, 1, 2])

# (c) 실제 1 중 오분류 개수 (행 기준!)
missed_1 = cm[1].sum() - cm[1, 1]
```

### ⚠️ 함정
- `accuracy_score(정답, 예측)` → **정답이 먼저**
- (c)에서 **열(`cm[:, 1]`)을 쓰면 틀려.** 열은 "1이라고 예측한 것"이야
- `labels=[0, 1, 2]`를 꼭 넣어야 어떤 품종이 하나도 없어도 3×3이 보장돼

### 확장: 다른 지표가 나오면
```python
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
# 다중 분류에선 average 필수
precision_score(y, p, average='macro')
recall_score(y, p, average='macro')
f1_score(y, p, average='macro')
print(classification_report(y, p))

# 혼동행렬로 직접 계산
recall_1    = cm[1, 1] / cm[1].sum()       # 실제 1 중 맞힌 비율 (행)
precision_1 = cm[1, 1] / cm[:, 1].sum()    # 1이라고 예측한 것 중 진짜 1 (열)
```

---

## 5. 분류 신경망 구성 [16점]

### 개념
- 구조: `13 → Linear(16) → ReLU → Linear(3)` → 출력 `(B, 3)` = 품종별 **점수(logits)**
- **CrossEntropyLoss 안에 Softmax가 들어 있어서** 모델 끝에 Softmax를 붙이면 안 돼
- 정답은 **정수 클래스 번호**(`torch.long`), 원-핫 아님
- 앞 층 출력 수 = 다음 층 입력 수 (16 → 16)

### 답안
```python
# (a) 신경망
net = nn.Sequential(
    nn.Linear(13, 16),
    nn.ReLU(),
    nn.Linear(16, 3),
)

# (b) 손실 함수
loss_fn = nn.CrossEntropyLoss()

# (c) 옵티마이저 (전체 가중치 = net.parameters())
optimizer = torch.optim.Adam(net.parameters(), lr=0.005)
```

### ⚠️ 함정
- `nn.Linear(입력, 출력)` 순서 헷갈리지 않기
- `nn.ReLU()` 괄호 빠뜨리면 에러
- `Adam(net.parameters(), ...)` — `parameters` **괄호** 꼭

### 문제 유형별 짝꿍 (변형 대비 ⭐)
| 문제 | 마지막 층 | 손실 | 정답 dtype |
|---|---|---|---|
| 다중 분류 (이번) | `Linear(?, 클래스 수)` | `nn.CrossEntropyLoss()` | `torch.long`, shape `(B,)` |
| 이진 분류 | `Linear(?, 1)` (Sigmoid 없음) | `nn.BCEWithLogitsLoss()` | `torch.float32`, shape `(B, 1)` |
| 이진 분류 (Sigmoid 포함) | `Linear(?, 1)` + `nn.Sigmoid()` | `nn.BCELoss()` | `torch.float32` |
| 회귀 | `Linear(?, 1)` | `nn.MSELoss()` | `torch.float32`, shape `(B, 1)` |

---

## 6. 반복 학습과 손실 기록 [18점] ⭐ 최고 배점

### 개념
- **배치:** 한 번에 넣는 묶음 (여기선 16개) / **1 epoch:** 학습 데이터 전체를 한 바퀴
- 학습 손실은 내려가고, 검증 손실이 다시 올라가기 시작하면 **과적합** 신호
- 기록용 리스트에 **딕셔너리**를 쌓고 → `pd.DataFrame(list)`로 바꾸면 표가 돼

### 답안
```python
# (a) 80 epoch 학습 + 기록
history = []
for epoch in range(1, 81):                     # ★ 1부터 80까지
    tr_loss = train_one_epoch(train_net, loader, train_loss_fn, train_opt)   # 먼저 학습
    va_loss = validation_loss(train_net, xv, yv, train_loss_fn)              # 그다음 검증
    history.append({'epoch': epoch, 'train_loss': tr_loss, 'valid_loss': va_loss})

# (b) 표 + 그래프
history_df = pd.DataFrame(history)
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(history_df['epoch'], history_df['train_loss'], label='train')
ax.plot(history_df['epoch'], history_df['valid_loss'], label='valid')
```

### ⚠️ 함정
- `range(80)`이면 0~79라서 **epoch 번호가 틀려.** `range(1, 81)`
- 딕셔너리 키 이름을 정확히: `'epoch'`, `'train_loss'`, `'valid_loss'`
- 다시 돌릴 땐 **준비 셀부터** 재실행 (안 그러면 이미 학습된 모델을 이어서 학습)
- 함수가 제공됐으니 **새로 짜지 말고 호출만**

### ⭐ 함수를 직접 짜라고 나올 수도 있어 (꼭 손으로 써 보기)
```python
def train_one_epoch(model, data_loader, criterion, opt):
    model.train()                         # 학습 모드 (Dropout ON)
    total, count = 0.0, 0
    for batch_x, batch_y in data_loader:
        opt.zero_grad()                   # ① 기울기 초기화
        scores = model(batch_x)           # ② 순전파
        loss = criterion(scores, batch_y) # ③ 손실
        loss.backward()                   # ④ 역전파
        opt.step()                        # ⑤ 가중치 갱신
        total += loss.item() * len(batch_y)   # 배치 크기로 가중 (마지막 배치가 작을 수 있어서)
        count += len(batch_y)
    return total / count                  # 평균 손실

def validation_loss(model, x, y, criterion):
    model.eval()                          # 평가 모드 (Dropout OFF)
    with torch.no_grad():                 # 기울기 기록 안 함
        value = criterion(model(x), y)
    return value.item()                   # 텐서 → 파이썬 실수
```

### 데이터 → DataLoader 준비 (준비 코드에 있던 것)
```python
train_set = TensorDataset(torch.tensor(X, dtype=torch.float32),
                          torch.tensor(y, dtype=torch.long))
loader = DataLoader(train_set, batch_size=16, shuffle=True)   # 학습용은 섞기
```

---

## 7. Dropout과 평가 모드 [10점]

### 개념
- **Dropout:** 학습 중 중간 출력 일부를 확률 p로 0으로 만듦 → 특정 뉴런 의존을 줄여 **과적합 완화**
- **`model.train()`** = Dropout 켜짐 (매번 결과 다름) / **`model.eval()`** = Dropout 꺼짐 (결과 일정)
- **`torch.no_grad()`** = 기울기 기록 안 함 → 메모리·속도 이득 (추론할 때)
- ⚠️ `eval()`과 `no_grad()`는 **다른 역할**이라 둘 다 써야 해

| | `model.eval()` | `torch.no_grad()` |
|---|---|---|
| 하는 일 | Dropout·BatchNorm을 평가 동작으로 | 기울기 계산 기록 끔 |
| 안 쓰면 | 같은 입력에도 출력이 매번 달라짐 | 메모리 낭비 (결과는 같음) |

### 답안
```python
# (a) Dropout 들어간 모델 (ReLU 바로 뒤)
drop_net = nn.Sequential(
    nn.Linear(13, 24),
    nn.ReLU(),
    nn.Dropout(p=0.2),
    nn.Linear(24, 3),
)

# (b) 평가 전용 예측 함수
def predict_scores(model, x):
    model.eval()
    with torch.no_grad():
        out = model(x)
    return out
```

### ⚠️ 함정
- `out = model(x)`는 **`with` 블록 안에** (들여쓰기 확인)
- 확률로 바꾸라는 말이 없으면 **Softmax 하지 마** (점수 그대로)
- 확인 셀에서 "두 출력 일치: True"가 나와야 eval이 제대로 된 거야

---

## 8. Softmax 확률로 재확인 시료 찾기 [8점]

### 개념
- **Softmax:** 점수(logits)를 **합이 1인 확률**로 변환. `dim=1` = 행(시료)마다
- **argmax:** 가장 큰 값의 **위치(=품종 번호)**. 동점이면 앞 번호를 줘서 "작은 번호 선택" 조건 자동 충족
- **불리언 마스크:** 조건(True/False) 배열로 원하는 원소만 골라냄

### 답안
```python
# (a) 확률과 예측 품종
probs = torch.softmax(scores, dim=1)          # (36, 3)
labels = torch.argmax(probs, dim=1)           # (36,)

# (b) 최대 확률 < 0.95 인 시료 ID
max_prob = probs.max(dim=1).values            # 시료별 최대 확률 (36,)
review_ids = ids[(max_prob < 0.95).numpy()]   # ★ 텐서 마스크 → numpy로 바꿔서 인덱싱
```

### ⚠️ 함정
- `dim=0`으로 하면 **열(품종)마다** 합이 1이 돼서 틀려 → 시료(행)마다는 **`dim=1`**
- "0.95 **미만**" → `<` (`<=` 아님)
- `ids`는 NumPy 배열이라 **마스크도 NumPy**로: `.numpy()`
- `probs.max(dim=1)`은 `(values, indices)` 두 개를 돌려줌 → `.values` 또는 `[0]`

### 같이 알아둘 텐서 연산
```python
scores.argmax(dim=1)                       # softmax 없이 argmax해도 결과 같음 (단조 증가)
(pred == y).float().mean().item()          # 텐서로 정확도 계산
torch.max(out, 1)                          # (최댓값, 인덱스)
t.shape / t.dtype / t.numpy() / t.tolist() / t.item()
```

---

## 9. 변형 대비 — 본시험에 나올 수 있는 것

모의고사가 "**사진과 리뷰 텍스트는 사용하지 않습니다**"라고 굳이 적은 걸 보면, 본시험엔 **이미지(CNN)나 텍스트**가 나올 수도 있어. 그래서 이것도 챙겨 두자.

### ① 이미지 → CNN
```python
cnn = nn.Sequential(
    nn.Conv2d(3, 16, kernel_size=3, padding=1),   # (B,3,32,32) → (B,16,32,32)
    nn.ReLU(),
    nn.MaxPool2d(2),                               # → (B,16,16,16)
    nn.Flatten(),                                  # → (B, 16*16*16)
    nn.Linear(16 * 16 * 16, 10),
)
```
- 출력 크기: `(W - K + 2P) / S + 1`, 풀링 2면 ÷2
- 이미지 텐서 모양은 **(배치, 채널, 높이, 너비)**

### ② 텍스트 → 토큰화 / 임베딩
```python
tokenizer = AutoTokenizer.from_pretrained('klue/bert-base')
enc = tokenizer(text, return_tensors='pt')
emb = nn.Embedding(num_embeddings=vocab_size, embedding_dim=64)
```

### ③ 정확도를 신경망 출력으로 직접 계산
```python
model.eval()
with torch.no_grad():
    pred = model(xv).argmax(dim=1)
acc = (pred == yv).float().mean().item()
```

### ④ 조기 종료 (검증 손실이 가장 낮을 때 기억)
```python
best = float('inf')
for epoch in range(1, 101):
    tr = train_one_epoch(...)
    va = validation_loss(...)
    if va < best:
        best, best_epoch = va, epoch
```

### ⑤ 기타 자주 쓰는 것
```python
history_df['valid_loss'].idxmin()          # 최소값의 인덱스
history_df.loc[history_df['valid_loss'].idxmin(), 'epoch']   # 그때 epoch
np.where(cond)[0]                          # 조건 만족하는 위치
torch.manual_seed(23)                      # 재현성
```

---

## 10. 🃏 시험 직전 30초 카드

```python
# 분할
train_df, valid_df = train_test_split(df, test_size=0.25, random_state=23, stratify=df['label'])
# 개수 / 그룹 평균
df['label'].value_counts().sort_index()
df.groupby('label')[['a', 'b']].mean()
# 산점도 / 선 그래프
ax.scatter(x, y, c=labels);  ax.plot(x, y, label='train')
# 싸이킷런
m = KNeighborsClassifier(n_neighbors=5); m.fit(X, y); m.predict(Xv)
accuracy_score(y, p);  confusion_matrix(y, p, labels=[0, 1, 2])   # 행=실제, 열=예측
# 신경망
nn.Sequential(nn.Linear(13, 16), nn.ReLU(), nn.Dropout(0.2), nn.Linear(16, 3))
nn.CrossEntropyLoss();  torch.optim.Adam(net.parameters(), lr=0.005)
# 학습 5줄
opt.zero_grad(); out = model(x); loss = crit(out, y); loss.backward(); opt.step()
# 평가
model.eval();  with torch.no_grad(): out = model(x)
# 확률 / 예측
torch.softmax(out, dim=1);  out.argmax(dim=1);  probs.max(dim=1).values
```

**체크리스트**
- [ ] 변수 이름 그대로? 반환 형식(Series / DataFrame / 배열 / 텐서) 맞나?
- [ ] `range(1, N+1)`?
- [ ] 분류 정답은 `long`, 회귀 정답은 `float32`?
- [ ] CrossEntropyLoss 앞에 Softmax 안 붙였나?
- [ ] 평가할 때 `eval()` + `no_grad()` 둘 다?
- [ ] softmax·argmax는 `dim=1`?
- [ ] 혼동행렬 **행 = 실제**?
- [ ] 제출 전 **커널 재시작 → 전체 실행**해서 결과 남겼나?
