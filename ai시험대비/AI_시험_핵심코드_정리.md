# 🧠 인공지능 시험 대비 — 반드시 알아야 할 코드 정리

> 학습자료 14개 노트북 전체에서 **시험에 코드 작성으로 나올 만한 것**만 골랐어. ⭐ 개수 = 중요도.
>
> 1장 기초(EDA·Scikit-learn / 신경망·MLP) → 2장 언어(토큰화·임베딩·허깅페이스 / LLM API·합성 데이터)
> → 3장 이미지(CNN·전이학습 / 파운데이션 모델) → 4장 LLM 앱(RAG / Agent) → 5장 모델 다루기(PEFT / 양자화)

---

## 🔥 0. 시험 직전 이것만은 꼭

| # | 이거 | 한 줄 |
|:--:|---|---|
| 1 | ⭐⭐⭐ **PyTorch 학습 루프 5줄** | `model(X)` → `criterion` → `zero_grad()` → `backward()` → `step()` (MLP·CNN·전이학습 전부 동일) |
| 2 | ⭐⭐⭐ **싸이킷런 3단계** | 생성 → `fit` → `predict` (+ `reshape(-1, 1)`) |
| 3 | ⭐⭐⭐ **train_test_split + 평가지표** | 회귀: MSE·R² / 분류: Accuracy·F1·AUC |
| 4 | ⭐⭐⭐ **손실함수 ↔ 출력층 짝꿍** | 다중분류 `CrossEntropyLoss`엔 Softmax 안 붙임 |
| 5 | ⭐⭐⭐ **AutoTokenizer → AutoModel → last_hidden_state** | shape `[1, 토큰수, 768]` |
| 6 | ⭐⭐⭐ **CNN 클래스 + 출력 크기 계산** | `출력 = 입력 - 커널 + 1`, 풀링은 ÷2 → `16*5*5` |
| 7 | ⭐⭐⭐ **전이학습 3줄** | 얼리기(`requires_grad=False`) → `model.fc` 교체 → 옵티마이저는 교체 **후에** |
| 8 | ⭐⭐⭐ **RAG 파이프라인** | Loader → Splitter → Embedding → Chroma → Retriever → LLM |
| 9 | ⭐⭐⭐ **LangGraph 4단계** | State(TypedDict) → Node 함수 → add_node/add_edge → compile/invoke |
| 10 | ⭐⭐ **Agent** | `@tool` + `create_react_agent` + `MemorySaver`/`thread_id` |
| 11 | ⭐⭐ **LoRA / 양자화 설정** | `get_peft_model(r, lora_alpha, target_modules)` / `BitsAndBytesConfig` 4옵션 |
| 12 | ⭐⭐ **Responses API + JSON 스키마** | `client.responses.create(...)` → `output_text` → `json.loads` |
| 13 | ⭐⭐ **nn.Embedding** | `(vocab_size, 768)` 짜리 "표에서 행 꺼내기" |

---

## 1. EDA & Scikit-learn (`easy-01-1`)

### 1-1. 데이터 훑어보기 ⭐⭐
```python
import seaborn as sns
df = sns.load_dataset('mpg')

df.info()       # 행/열 개수, 컬럼 타입, 결측치(Non-Null 개수) 확인
df.describe()   # 평균(mean), 표준편차(std), 최솟값, 사분위수, 최댓값
```

### 1-2. 상관관계 + 히트맵 ⭐⭐
```python
df['weight'].corr(df['acceleration'])     # 두 컬럼 상관계수 (-1 ~ 1)

corr = df.corr(numeric_only=True)          # 숫자 컬럼끼리 상관계수 표
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
```
- 상관계수 **+1 = 같이 증가 / -1 = 반대로 / 0 = 관계 없음**
- **상관관계 ≠ 인과관계** (이론 단골)

### 1-3. 분포 / 분산 ⭐
```python
sns.histplot(df['weight'], bins=20, kde=True)   # 분포 = "모양"

np.var(data)              # numpy: ddof=0 (모분산, n으로 나눔)
pd.Series(data).var()     # pandas: ddof=1 (표본분산, n-1로 나눔) → 값이 다름!
```
- 표준편차 = √분산 (원래 단위로 되돌리려고 루트 씌움)

### 1-4. 싸이킷런 3단계 패턴 ⭐⭐⭐
```python
from sklearn.linear_model import LinearRegression, LogisticRegression

X = tips['total_bill'].values.reshape(-1, 1)   # ★ X는 반드시 2차원! (행 n개, 열 1개)
y = tips['tip'].values                          # y는 1차원 OK

model = LinearRegression()   # ① 생성
model.fit(X, y)              # ② 학습
y_hat = model.predict(X)     # ③ 예측

# 로지스틱 회귀 (분류) — 확률이 필요하면 predict_proba
model = LogisticRegression()
model.fit(X, y)
prob = model.predict_proba(X_new)[:, 1]   # [0일 확률, 1일 확률] 중 1(합격)일 확률만
```
- `reshape(-1, 1)` 의미: "행 개수는 알아서(-1), 열은 1개"

### 1-5. 표준화 (StandardScaler) ⭐⭐⭐
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)                     # 평균·표준편차 "계산"만 (train에만!)
X_train_std = scaler.transform(X_train) # 실제 변환
X_test_std  = scaler.transform(X_test)  # test는 transform만! fit 하면 데이터 유출

y_pred = scaler_y.inverse_transform(y_pred_std)   # 표준화된 값 → 원래 단위로 복원
```
- 공식: `z = (x - 평균) / 표준편차` → 평균 0, 표준편차 1
- ⚠️ 표준화 결과는 0~1 아님! (0~1로 만드는 건 **Min-Max 정규화**)
- ⚠️ 분포 **모양은 안 바뀜** (위치와 폭만 바뀜)
- 트리 계열 모델(결정트리, 랜덤포레스트)은 표준화 거의 영향 없음

### 1-6. 데이터 나누기 ⭐⭐⭐
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y   # stratify: 클래스 비율 유지 (분류)
)

# Train 80 / Val 10 / Test 10 → 두 번 나누기
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test     = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
```
- **반환 순서 주의**: `X_train, X_test, y_train, y_test`
- Test는 **마지막에 딱 한 번**만 (자꾸 보면 데이터 유출)

### 1-7. 평가지표 ⭐⭐⭐
```python
from sklearn.metrics import mean_squared_error, r2_score             # 회귀
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score   # 분류

mse = mean_squared_error(y_test, model.predict(X_test))   # 0에 가까울수록 좋음
r2  = r2_score(y_test, model.predict(X_test))             # 1에 가까울수록 좋음

acc = accuracy_score(y_test, y_pred)
f1  = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_prob)   # ★ AUC는 예측 "확률"을 넣음!
```
- **과적합**: Train 높고 Test 낮음 (족보만 외움) / **과소적합**: 둘 다 낮음
- 불균형 데이터(정상 99 : 암 1)에선 Accuracy 믿으면 안 됨 → F1 사용
- 정밀도 = "1이라고 한 것 중 진짜 1" / 재현율 = "진짜 1 중 찾아낸 비율"

---

## 2. PyTorch · 신경망 · MLP (`easy-01-2`)

### 2-1. 텐서 & 자동미분(Autograd) ⭐⭐
```python
import torch
a = torch.tensor([[1, 2], [3, 4]])
a.shape          # torch.Size([2, 2])
a @ a            # 행렬곱
loss.item()      # 텐서에서 숫자 하나 꺼내기

x = torch.tensor(2.0, requires_grad=True)   # 미분 추적 ON
y = x**2 + 3*x + 1
y.backward()     # 역전파 → dy/dx 계산
print(x.grad)    # 2*2 + 3 = 7.0

x.grad.zero_()   # ★ 기울기는 "누적"되니까 초기화 필요

with torch.no_grad():   # 미분 추적 OFF (평가·추론·시각화할 때)
    y_hat = model(X)
```
- Tensor = NumPy 배열 + **GPU 연산** + **자동 미분**

### 2-2. 손실함수 ↔ 출력층 짝꿍 ⭐⭐⭐ (실수 1위)
| 문제 | 마지막 층 | 손실함수 |
|---|---|---|
| 회귀 (숫자 예측) | 없음 | `nn.MSELoss()` |
| 이진 분류 | `nn.Sigmoid()` | `nn.BCELoss()` |
| 이진 분류 (권장) | 없음 | `nn.BCEWithLogitsLoss()` (Sigmoid 내장) |
| 다중 분류 | **없음** | `nn.CrossEntropyLoss()` (**Softmax 내장**) |

### 2-3. 학습 루프 (모든 딥러닝의 기본 문법) ⭐⭐⭐
```python
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(1, 1)                          # y = Wx + b
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(2000):
    y_hat = model(X)              # ① 순전파
    loss = criterion(y_hat, y)    # ② 손실 계산
    optimizer.zero_grad()         # ③ 기울기 초기화 (누적 방지)
    loss.backward()               # ④ 역전파 (미분 계산)
    optimizer.step()              # ⑤ W, b 업데이트
```
> 🧠 **순서 외우기**: 예측 → 채점 → 지우개 → 원인분석 → 고치기

### 2-4. Sequential + ReLU (MLP) ⭐⭐⭐
```python
model = nn.Sequential(
    nn.Linear(1, 64),   nn.ReLU(),
    nn.Linear(64, 128), nn.ReLU(),
    nn.Linear(128, 1)            # 앞 층 출력 수 = 다음 층 입력 수 (64→64, 128→128)
)
optimizer = optim.Adam(model.parameters(), lr=0.005)

# 로지스틱 회귀를 파이토치로
model = nn.Sequential(nn.Linear(1, 1), nn.Sigmoid())
criterion = nn.BCELoss()
```
- **활성화 함수 없이 Linear만 쌓으면?** → `W2(W1x+b1)+b2 = (W2W1)x + (...)` = 결국 직선 1개. 100층 쌓아도 1층이랑 같음
- **ReLU**: 음수 → 0, 양수 → 그대로. 기울기 소실 문제 완화
- **XOR**은 직선 1개(퍼셉트론, 로지스틱 회귀)로 못 풂 → 은닉층 필요

### 2-5. MNIST 숫자 분류기 (총정리 코드) ⭐⭐⭐
```python
from torch.utils.data import DataLoader

train_df = pd.read_csv('sample_data/mnist_train_small.csv', header=None)  # header=None 중요!
X_train = torch.tensor(train_df.iloc[:, 1:].values, dtype=torch.float32) / 255.0  # 픽셀 0~1로
y_train = torch.tensor(train_df.iloc[:, 0].values, dtype=torch.long)              # 정답은 long!

train_loader = DataLoader(list(zip(X_train, y_train)), batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Linear(784, 256), nn.ReLU(),   # 28×28 = 784 픽셀을 한 줄로 펴서 입력
    nn.Linear(256, 128), nn.ReLU(),
    nn.Linear(128, 10)                # 숫자 0~9 → 출력 10개 (Softmax 안 붙임!)
)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(5):
    for X_batch, y_batch in train_loader:
        outputs = model(X_batch)
        loss = loss_fn(outputs, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

torch.save(model.state_dict(), 'model.pth')     # 저장

# --- 불러와서 추론 ---
model.load_state_dict(torch.load('model.pth'))
model.eval()                                    # 평가 모드
with torch.no_grad():
    outputs = model(X_batch)
    preds = torch.argmax(outputs, dim=1)        # 10개 점수 중 가장 큰 위치 = 예측 숫자
```
- Cross Entropy는 **정답 클래스에 준 확률**만 봄 (Max 아님!)
- 배치 = 한 번에 넣는 묶음 / 이터레이션 = 배치 1번 학습 / 에포크 = 전체 데이터 1바퀴

---

## 3. 토큰화 (`2_0`, `2_1`)

### 3-1. 사전학습 토크나이저 쓰기 (AutoTokenizer) ⭐⭐⭐
```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('klue/bert-base')

encoded = tokenizer('안녕하세요. 반가워요')
# {'input_ids': [2, 5891, ...,  3], 'token_type_ids': [0,...], 'attention_mask': [1,...]}

tokenizer.convert_ids_to_tokens(encoded['input_ids'])
# ['[CLS]', '안녕', '##하', '##세요', '.', ..., '[SEP]']   ← [CLS], [SEP] 자동 추가

tokenizer.tokenize('자연어처리')   # ['자연', '##어', '##처리']
tokenizer.vocab_size               # 32000
len(tokenizer)                     # 추가 토큰까지 포함한 실제 크기
```
- `##` = "앞 토큰에 이어 붙는 조각" (WordPiece 서브워드)
- `attention_mask`: 진짜 토큰 1, 패딩 0

### 3-2. 토크나이저 직접 학습 (BertWordPieceTokenizer) ⭐⭐
```python
from tokenizers import BertWordPieceTokenizer

tokenizer = BertWordPieceTokenizer(lowercase=False, strip_accents=False)
tokenizer.train(
    files='nsmc.txt',
    vocab_size=30000,          # 사전 크기
    min_frequency=2,           # 최소 2번 이상 등장해야 사전에 넣음
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],  # 순서대로 0~4번 ID
)
tokenizer.save_model('.', 'nsmc')          # → nsmc-vocab.txt 저장

enc = tokenizer.encode('나는 개발자 입니다!')
enc.tokens    # ['나는', '개발', '##자', '입니다', '!']
enc.ids       # [2371, 9228, 1094, ...]
tokenizer.decode(enc.ids)

# 저장한 사전으로 다시 불러오기 → 이때는 [CLS]/[SEP]가 자동으로 붙음
tok2 = BertWordPieceTokenizer('nsmc-vocab.txt', lowercase=False, strip_accents=False)

tokenizer.get_vocab_size() / tokenizer.get_vocab()   # 사전 크기 / {토큰: ID}
tokenizer.token_to_id('영화') / tokenizer.id_to_token(45)   # 없는 단어면 None!
```

### 3-3. 특수 토큰 (이론 단골) ⭐⭐
| 토큰 | 역할 |
|---|---|
| `[CLS]` | 문장 시작, 문장 전체를 대표 |
| `[SEP]` | 문장 끝 / 두 문장 구분 |
| `[PAD]` | 배치 길이 맞추려고 채우는 빈칸 |
| `[UNK]` | 사전에 없고 쪼갤 수도 없는 단어 |
| `[MASK]` | BERT 사전학습 때 단어 가리기 |

- **OOV** = 사전에 없는 단어 → 서브워드(BPE, WordPiece)로 최소화
- BPE: 빈도 높은 쌍 병합 (GPT 계열) / WordPiece: 확률 기반 병합 (BERT 계열)

### 3-4. 데이터 전처리 (pandas) ⭐
```python
data = pd.read_csv('ratings.txt', sep='\t')   # 탭으로 구분된 파일
data = data.dropna()                           # 결측치 제거
data = data['document']                        # 리뷰 열만
with open('nsmc.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(data))                   # 한 줄에 리뷰 하나 (to_csv 쓰면 따옴표 오염)
```

---

## 4. 임베딩 (`2_0`, `2_2`, `2_3`)

### 4-1. 사전학습 모델로 문맥 임베딩 뽑기 ⭐⭐⭐
```python
import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('klue/bert-base')
model     = AutoModel.from_pretrained('klue/bert-base')   # ★ 토크나이저와 이름 똑같이!

encoded = tokenizer(text, return_tensors='pt')   # 'pt' = PyTorch 텐서로
with torch.no_grad():
    output = model(**encoded)                    # 딕셔너리 풀어서 전달

emb = output.last_hidden_state
emb.shape   # torch.Size([1, 25, 768]) = [배치, 토큰 수, 벡터 차원]
```

### 4-2. 임베딩 층 (nn.Embedding) ⭐⭐⭐
```python
import torch.nn as nn

vocab_size = tokenizer.get_vocab_size()   # 하드코딩 말고 실제 크기 (작으면 IndexError)
embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim=768)
embedding_layer.weight.shape              # (vocab_size, 768)

vec = embedding_layer(torch.tensor([45]))   # = embedding_layer.weight[45] (표에서 45번 행 꺼내기)
```
- 원핫: 30000차원, 대부분 0, 단어끼리 유사도 항상 0 → **임베딩**: 768차원 실수 벡터

### 4-3. 코사인 유사도로 비슷한 단어 찾기 ⭐⭐
```python
import torch.nn.functional as F

target_vector = embedding_layer.weight[tokenizer.token_to_id('영화')]
with torch.no_grad():
    sims = F.cosine_similarity(target_vector.unsqueeze(0),   # [768] → [1, 768]
                               embedding_layer.weight,        # [vocab, 768]
                               dim=1)
    top_scores, top_idx = torch.topk(sims, k=6)   # 1등은 자기 자신이라 k+1
```
- 코사인 유사도: 1(같은 방향) ~ -1(반대 방향)

### 4-4. 사전학습 임베딩 이식 (전이학습 맛보기) ⭐
```python
pretrained_emb = pretrained_model.embeddings.word_embeddings.weight   # 입력 임베딩 표
pretrained_vocab = pretrained_tokenizer.get_vocab()   # ★ 반복문 밖에서 한 번만!

with torch.no_grad():
    for token, token_id in tokenizer.get_vocab().items():
        pid = pretrained_vocab.get(token)            # 양쪽 사전에 다 있는 단어만
        if pid is not None:
            embedding_layer.weight[token_id] = pretrained_emb[pid]
```

### 4-5. "임베딩" 3가지 구분 (이론 단골) ⭐⭐
| 이름 | 코드 | 문맥 반영 | 위치 |
|---|---|---|---|
| 임베딩 층 | `nn.Embedding` / `model.embeddings.word_embeddings` | ❌ 단어당 벡터 1개 | 모델 입구 |
| 문맥 임베딩 | `model(**inputs).last_hidden_state` | ✅ 문장마다 달라짐 | 모델 출구 |

- 정적 임베딩(Word2Vec: CBOW·Skip-gram, GloVe) → "밤(야간)"과 "밤(견과류)" 구분 못 함
- BERT = 트랜스포머 **인코더**만 + **양방향** / Positional Embedding = 순서 정보

---

## 5. LLM API 사용 (`2_1_Settings`)

### 5-1. API 키 불러오기 ⭐⭐
```python
from dotenv import load_dotenv
from os import getenv

load_dotenv()                 # .env 파일 → 환경 변수로 등록
GMS_KEY = getenv('GMS_KEY')
```
- 키는 코드에 직접 쓰지 않음, `.gitignore`에 `.env` 추가

### 5-2. Responses API 호출 ⭐⭐⭐
```python
from openai import OpenAI

client = OpenAI(api_key=GMS_KEY,
                base_url='https://gms.ssafy.io/gmsapi/api.openai.com/v1/')

response = client.responses.create(
    model='gpt-5-nano',
    input='안녕?',                       # 질문
    instructions='너는 영화 전문가야',     # 시스템 프롬프트 (선택)
    reasoning={'effort': 'low'},        # low / medium / high (temperature 대신)
)
print(response.output_text)             # ★ 결과 꺼내기
```
| | Chat Completions (옛날) | **Responses (권장)** |
|---|---|---|
| 메서드 | `chat.completions.create()` | `responses.create()` |
| 입력 | `messages=[...]` | `input='...'` |
| 시스템 | `role: 'system'` | `instructions=` |
| 결과 | `choices[0].message.content` | `output_text` |

### 5-3. 스트리밍 ⭐
```python
stream = client.responses.create(model='gpt-5-nano', input='...', stream=True)
for event in stream:
    if event.type == 'response.output_text.delta':
        print(event.delta, end='')
```

### 5-4. JSON 구조화 출력 ⭐⭐⭐
```python
import json

text_format = {
    'format': {
        'type': 'json_schema',
        'name': 'capital_info',              # 영문/숫자/_ 만
        'strict': True,
        'schema': {
            'type': 'object',
            'properties': {
                'capital': {'type': 'string'},
                'translation': {'type': 'string'},
            },
            'required': ['capital', 'translation'],   # ① 모든 키가 required에
            'additionalProperties': False,            # ② 반드시 False
        },
    },
}
response = client.responses.create(model='gpt-5-nano', input='한국의 수도는?', text=text_format)
data = json.loads(response.output_text)   # ★ 문자열 → 딕셔너리 (안 하면 data['capital'] 에러)

json.dumps(data, ensure_ascii=False)      # 딕셔너리 → 문자열 (한글 깨짐 방지)
```

### 5-5. 비동기 (참고) ⭐
```python
import asyncio
results = await asyncio.gather(*tasks, return_exceptions=True)  # 여러 요청 동시에
# .py 파일에서는 asyncio.run(main())
```

### 5-6. 에러 코드 ⭐
`401` 키 문제 / `400` 요청 내용 잘못(모델명·파라미터·스키마) / `404` 주소 잘못 / `429` 너무 많이 보냄 / `500·503` 서버 문제

---

## 6. 합성 데이터 & LLM as a Judge (`2_2_Synthesis_data`)

### 6-1. 호출 함수 감싸기 ⭐⭐
```python
def chat_completion(prompt, system_prompt=None, model='gpt-5-nano',
                    effort='medium', text_format=None):
    kwargs = {'model': model, 'input': prompt, 'reasoning': {'effort': effort}}
    if system_prompt:
        kwargs['instructions'] = system_prompt
    if text_format:
        kwargs['text'] = text_format
    return client.responses.create(**kwargs).output_text
```

### 6-2. 프롬프팅 기법 ⭐⭐
- **Zero-shot**: 예시 없이 질문만
- **Few-shot**: 입출력 예시 2~5개 보여주기 (형식·말투 유도)
- **CoT**: "단계별로 생각해봐" → 추론 정확도 ↑
- **Role**: "너는 ○○ 전문가야" (system prompt)
- 프롬프트 기본 구조 = **역할 + 목표 + 조건**

### 6-3. LLM as a Judge ⭐⭐
```python
def evaluate_with_llm(instruction, output, criteria):
    user_prompt = f'입력 프롬프트: {instruction}\n모델 답변: {output}\n평가 기준: {criteria}'
    result = chat_completion(user_prompt, JUDGE_SYSTEM_PROMPT,
                             effort='low', text_format=judge_text_format)  # score, comment
    return json.loads(result)
```
- 방식: **Pointwise**(점수) / **Pairwise**(A vs B) / **Reference-based**(정답 대조)
- 편향: 자기 편향, 위치 편향 등 → LLM 채점은 1차 필터, 최종은 사람
- **합성** = 새 데이터 생성 / **증강** = 기존 데이터 변형
- 합성 데이터만 반복 학습하면 **모델 붕괴** → 실제 데이터와 섞어 쓰기

---

## 7. CNN — 이미지 분류기 (`easy-03-1`)

### 7-1. 데이터 준비 (torchvision) ⭐⭐
```python
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.ToTensor(),                                   # 이미지 → 텐서 (0~1)
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),  # 채널(RGB)별 정규화 → -1~1
])
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True)
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False)   # 테스트는 섞을 필요 없음
```
- CIFAR-10: 10개 클래스, 이미지 **3 × 32 × 32** (채널, 높이, 너비)
- PyTorch는 **(C, H, W)**, matplotlib은 **(H, W, C)** → 그릴 때 `np.transpose(img, (1, 2, 0))`

### 7-2. CNN 모델 정의 (nn.Module 클래스) ⭐⭐⭐
```python
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)        # (입력 채널, 출력 채널=필터 수, 커널 크기)
        self.pool  = nn.MaxPool2d(2, 2)        # 2×2 중 최댓값 → 크기 절반
        self.conv2 = nn.Conv2d(6, 16, 5)       # ★ conv1 출력(6) = conv2 입력(6)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # 평탄화된 크기 = 400
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)           # 클래스 10개

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)                # 배치 차원(0)은 두고 나머지를 한 줄로
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)                     # Softmax 없음 (CrossEntropyLoss가 해줌)

net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
```

### 7-3. ⭐ 출력 크기 계산 (계산 문제 단골) ⭐⭐⭐
**공식 (패딩 0, stride 1): `출력 = 입력 - 커널 + 1`**, MaxPool2d(2,2)는 **÷ 2**

| 단계 | 크기 | 계산 |
|---|---|---|
| 입력 | 3 × 32 × 32 | |
| conv1 (5×5) | 6 × 28 × 28 | 32 - 5 + 1 |
| pool | 6 × 14 × 14 | 28 ÷ 2 |
| conv2 (5×5) | 16 × 10 × 10 | 14 - 5 + 1 |
| pool | 16 × 5 × 5 | 10 ÷ 2 |
| flatten | **400** | 16 × 5 × 5 |

- 크기 안 맞으면 `mat1 and mat2 shapes cannot be multiplied` 에러
- `padding=2` 주면 5×5 커널이어도 32 → 32 유지

### 7-4. 학습 & 정확도 평가 ⭐⭐⭐
```python
for epoch in range(2):
    for inputs, labels in trainloader:
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct, total = 0, 0
with torch.no_grad():
    for images, labels in testloader:
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)       # = outputs.argmax(1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(f'Accuracy: {100 * correct / total}%')
```

### 7-5. GPU 사용 ⭐⭐
```python
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
net = Net().to(device)
inputs, labels = inputs.to(device), labels.to(device)   # ★ 데이터도 같은 장치로!
```
- 모델만 GPU, 데이터는 CPU면 `Expected all tensors to be on the same device` 에러

### 7-6. 전이학습 (Transfer Learning) ⭐⭐⭐
```python
from torchvision import models

model = models.resnet18(weights='IMAGENET1K_V1')        # ImageNet으로 사전학습된 모델

# 방식 ① 특징 추출 (= 리니어 프로빙): 몸통은 얼리고 마지막 층만 학습
for param in model.parameters():
    param.requires_grad = False                         # 얼리기

model.fc = nn.Linear(model.fc.in_features, 10)          # ★ 마지막 층 교체 (1000종 → 10종)
model = model.to(device)
optimizer = optim.SGD(model.fc.parameters(), lr=0.01, momentum=0.9)   # ★ 교체 "후에" 생성

# 방식 ② 미세조정 (Fine-tuning): 얼리지 않고 전체를 작은 lr로 학습
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 입력 전처리는 사전학습 때와 똑같이 (ImageNet 표준값)
transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

model.train()   # 학습 모드
model.eval()    # 평가 모드 (Dropout/BatchNorm 고정)
```
| | 특징 추출 | 미세조정 |
|---|---|---|
| 학습 범위 | 마지막 층만 (`requires_grad=False`) | 전체 |
| 속도·메모리 | 빠르고 가벼움 | 느리고 무거움 |
| 학습률 | 비교적 큼 | **작게** (크면 파괴적 망각) |

**전이학습 3원칙**: ① 전처리를 사전학습 모델에 맞춘다 ② 마지막 층은 반드시 교체 ③ 옵티마이저는 모델 수정 후에 만든다

- **CNN = 특징 추출부(Conv + Pool) + 분류부(MLP)** → 앞부분을 가져다 쓰는 게 전이학습
- CNN이 MLP보다 나은 이유: 이미지를 펴지 않아서 **인접 픽셀 관계**를 살리고, 같은 필터를 재사용해서 **파라미터가 적음**

---

## 8. 이미지 파운데이션 모델 (`03-2`)

### 8-1. Stable Diffusion (텍스트 → 이미지) ⭐
```python
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5',
                                               torch_dtype=torch.float16).to(device)
result = pipe(
    'A watercolor painting of a red fox',          # positive prompt
    negative_prompt='low quality, blurry, text',   # 피하고 싶은 것
    guidance_scale=7.5,         # 프롬프트를 얼마나 강하게 따를지
    num_inference_steps=20,     # 노이즈 제거 단계 수 (품질 ↔ 속도)
    num_images_per_prompt=2,
)
images = result.images          # PIL 이미지 리스트
```
- 동작 원리: 랜덤 노이즈에서 시작 → 텍스트 조건에 맞게 **점진적으로 노이즈 제거** (diffusion)

### 8-2. CLIP (이미지 ↔ 텍스트 유사도) ⭐⭐
```python
from transformers import CLIPProcessor, CLIPModel
processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')
model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32').to(device)

labels = ['a watercolor painting of a fox', 'a watercolor painting of a dog', 'a photo of a fox']
inputs = processor(text=labels, images=image, return_tensors='pt', padding=True).to(device)
with torch.no_grad():
    outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)   # 각 문장일 확률
best = labels[probs.argmax(dim=1).item()]
```
- CLIP = 이미지와 텍스트를 **같은 임베딩 공간**에 넣고 비교 → 추가 학습 없이 분류 가능 (제로샷)

### 8-3. ResNet50으로 예측 + ImageFolder ⭐
```python
resnet50 = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2).to(device).eval()
img_tensor = preprocess(image).unsqueeze(0).to(device)   # [3,224,224] → [1,3,224,224] 배치 차원 추가
probs = torch.nn.functional.softmax(resnet50(img_tensor), dim=1)
top5_prob, top5_idx = probs.topk(5)

from torchvision.datasets import ImageFolder
train_dataset = ImageFolder('data/train', transform=train_transforms)  # ★ 폴더 이름 = 클래스 이름
train_dataset.classes   # ['dog', 'fox']

train_transforms = transforms.Compose([       # 데이터 증강은 "학습용"에만
    transforms.RandomResizedCrop((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
```
- **파운데이션 모델**: 대규모 데이터로 사전학습된 범용 모델 (GPT, BERT, CLIP, ResNet, Stable Diffusion)

---

## 9. RAG (`04-1`)

### 9-1. LangChain으로 LLM·임베딩 준비 ⭐⭐
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
llm = ChatOpenAI(model='gpt-5-nano', api_key=GMS_KEY, base_url=GMS_BASE_URL,
                 use_responses_api=True, reasoning_effort='low')
embeddings = OpenAIEmbeddings(model='text-embedding-3-small', api_key=GMS_KEY, base_url=GMS_BASE_URL)

llm.invoke('안녕?')
embeddings.embed_query('텍스트')          # 벡터 1개 (1536차원)
embeddings.embed_documents([...])        # 벡터 여러 개
```

### 9-2. RAG 파이프라인 (준비 단계) ⭐⭐⭐
```python
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# ① Loader: PDF → Document 리스트 (doc.page_content, doc.metadata)
docs = PyMuPDF4LLMLoader('data/파일.pdf').load()

# ② Splitter: 긴 문서를 조각(chunk)으로
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,       # 조각 최대 글자 수
    chunk_overlap=50,     # 조각끼리 겹치는 부분 (경계에서 문장 잘림 방지, 보통 10~20%)
    separators=['\n\n', '\n', '.', ' ', ''],   # 문단 → 줄 → 문장 → 단어 → 글자 순으로 시도
)
chunks = splitter.split_documents(docs)

# ③ Embedding + ④ Vector Store
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, collection_name='yes24')

# ⑤ Retriever
retriever = vectorstore.as_retriever(search_kwargs={'k': 3})   # 가장 비슷한 3개
results = retriever.invoke('배송이 늦으면 보상?')
```

### 9-3. 프롬프트 템플릿 ⭐⭐
```python
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ('system', '자료를 참고해 답하세요. 자료에 없으면 없다고 하세요.\n[참고 자료]\n{context}'),
    ('human', '{question}'),
])
messages = prompt.format_messages(context=context, question=question)
response = llm.invoke(messages)
```

### 9-4. 코사인 유사도 (NumPy) ⭐⭐
```python
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

### 9-5. LangGraph 4단계 패턴 ⭐⭐⭐
```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1단계: State 정의 (노드끼리 공유하는 "칠판")
class RAGState(TypedDict):
    question: str
    context: str
    answer: str

# 2단계: Node 함수 (State를 받아서 "바꿀 필드만" dict로 반환)
def retrieve(state: RAGState):
    docs = retriever.invoke(state['question'])
    return {'context': '\n\n'.join(d.page_content for d in docs)}

def generate(state: RAGState):
    msgs = prompt.format_messages(context=state['context'], question=state['question'])
    return {'answer': llm.invoke(msgs).content}

# 3단계: Graph 구성
workflow = StateGraph(RAGState)
workflow.add_node('retrieve', retrieve)
workflow.add_node('generate', generate)
workflow.add_edge(START, 'retrieve')
workflow.add_edge('retrieve', 'generate')
workflow.add_edge('generate', END)

# 4단계: 컴파일 + 실행
graph = workflow.compile()
result = graph.invoke({'question': '총알배송이 뭔가요?'})
result['answer']

# [참고] 조건부 엣지: 함수 반환값에 따라 다른 노드로
workflow.add_conditional_edges('retrieve', route_fn, {'generate': 'generate', 'fallback': 'fallback'})
```

### 9-6. RAG 이론 ⭐⭐
- **LLM의 3가지 한계**: 환각 / 최신 정보 부재 / 도메인 지식 부족
- 환각 원인: LLM은 검색이 아니라 **다음 토큰 예측**만 함
- **키워드 검색**: 글자가 똑같아야 찾음 / **의미 검색**: 임베딩 유사도로 동의어도 찾음
- RAG = "오픈북 시험". 출처 제시 가능, 문서만 바꾸면 최신화
- RAG 한계: **검색이 틀리면 답도 틀림** → 디버깅은 `retriever.invoke()`로 검색부터 확인
- **LangChain = 부품 상자**, **LangGraph = 조립 설계도** (분기·반복 가능)

---

## 10. AI Agent (`04-2`)

### 10-1. Tool 만들기 ⭐⭐⭐
```python
from langchain_core.tools import tool

@tool
def get_order_status_tool(order_id: str) -> str:
    """주문 상태를 조회한다. 주문번호(예: ORD001)를 입력하면 현재 상태를 반환한다."""
    return get_order_status(order_id)
# ★ docstring = LLM이 읽는 "도구 설명서" (부실하면 도구를 잘못 고름)

tools = [get_order_status_tool, issue_coupon_tool]
llm_with_tools = llm.bind_tools(tools)          # LLM에게 도구 목록 알려주기
response = llm_with_tools.invoke('ORD001 상태 확인해줘')
response.tool_calls                              # [{'name': ..., 'args': {...}}]
```

### 10-2. ReAct Agent ⭐⭐⭐
```python
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model=llm, tools=tools, prompt='당신은 고객 서비스 에이전트입니다.')
result = agent.invoke({'messages': [{'role': 'user', 'content': 'ORD001 확인하고 지연이면 쿠폰 발급해줘'}]})
result['messages'][-1]      # 최종 답변
```

### 10-3. Memory ⭐⭐⭐
```python
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
agent = create_react_agent(model=llm, tools=tools, prompt='...', checkpointer=memory)

config = {'configurable': {'thread_id': 'user123'}}   # ★ 같은 thread_id = 같은 대화
agent.invoke({'messages': [{'role': 'user', 'content': '내 주문번호는 ORD001이야'}]}, config=config)
agent.invoke({'messages': [{'role': 'user', 'content': '그 주문 상태 알려줘'}]}, config=config)  # 기억함
```
- `MemorySaver`는 메모리에만 저장 → 프로세스 끝나면 사라짐 (실무는 SqliteSaver 등)

### 10-4. Multi-Agent: Reflection 루프 ⭐⭐
```python
def should_continue(state):
    if state['reflection_count'] >= MAX + 1: return 'end'   # ★ 무한 루프 방지
    if state.get('final_result'):            return 'end'
    return 'worker'

workflow.add_edge(START, 'planner')
workflow.add_edge('planner', 'worker')
workflow.add_edge('worker', 'reflection')
workflow.add_conditional_edges('reflection', should_continue, {'end': END, 'worker': 'worker'})
```

### 10-5. Agent 이론 ⭐⭐
- **Agent 4요소**: LLM(두뇌) + Tool(손) + Memory(기억) + Plan(전략)
- RAG는 흐름 고정 / Agent는 **LLM이 흐름을 동적으로 결정**
- **흐름을 미리 그릴 수 있으면 Agent 쓰지 마라** (RAG나 일반 코드가 싸고 빠름)
- **ReAct** = Thought → Action → Observation 반복 = **CoT + Tool-use**
- 도구 1회 사용 = LLM 최소 2회 호출 (도구 선택 + 결과로 답변 생성)
- **3중 보호**: 입력 가드레일 → **검증 로직(도구 함수 안, 가장 중요)** → 출력 가드레일
- **HITL**(Human-in-the-Loop): 환불·삭제 같은 고위험 행동은 사람 승인
- Multi-Agent 패턴: Planner-Worker / Supervisor-Worker / Reflection / Debate / Pipeline
- 도구는 예외를 던지지 말고 **에러 문자열을 반환** (그래야 Agent가 안 멈춤)

---

## 11. PEFT · LoRA · QLoRA (`05-1`)

### 11-1. 4비트로 모델 로딩 + LoRA 붙이기 ⭐⭐⭐
```python
from unsloth import FastModel
model, tokenizer = FastModel.from_pretrained(
    model_name='unsloth/gemma-3-1b-it-unsloth-bnb-4bit',
    max_seq_length=1024,
    load_in_4bit=True,          # ← QLoRA의 Q (4비트 양자화)
)
model = FastModel.get_peft_model(
    model,
    r=8,                        # rank (작을수록 가벼움)
    lora_alpha=16,              # 스케일링: α/r = 2배
    lora_dropout=0.0,
    target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj',   # Attention
                    'gate_proj', 'up_proj', 'down_proj'],      # MLP
)
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)   # ~1%만 학습
```

### 11-2. Chat Template ⭐⭐
```python
messages = [{'role': 'system', 'content': '지시'},
            {'role': 'user', 'content': '입력'},
            {'role': 'assistant', 'content': '정답'}]   # ★ assistant 부분을 학습

# 학습용: 정답이 이미 있으니 add_generation_prompt=False
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
# 추론용: 모델이 이어서 답하도록 add_generation_prompt=True
text = tokenizer.apply_chat_template(messages[:2], tokenize=False, add_generation_prompt=True)
```

### 11-3. 학습 (SFTTrainer) ⭐
```python
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    model=model, tokenizer=tokenizer, train_dataset=dataset,
    args=SFTConfig(
        dataset_text_field='text',
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,   # 4번 모아서 업데이트 → 실효 배치 2×4 = 8
        learning_rate=5e-5,
        num_train_epochs=1,
    ),
)
trainer.train()
```

### 11-4. 생성(추론) 후 새 토큰만 디코딩 ⭐⭐
```python
inputs = tokenizer(text, return_tensors='pt').to('cuda')
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50, do_sample=False)
answer = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:],   # ★ 입력 길이 이후만
                          skip_special_tokens=True)
```

### 11-5. LoRA 이론 (계산 문제 가능) ⭐⭐⭐
- 수식: **`h = Wx + (α/r) · BAx`** — W는 고정 ❄️, **B와 A만 학습** 🔥
- 모양: **B = d × r, A = r × d** → B×A = d × d (W와 같은 크기)
- 학습 파라미터: **`2 × d × r`** (예: d=4096, r=8 → 65,536개 = 전체 1,677만 개의 0.39%)
- 초기화: **A = 랜덤, B = 0** → 시작할 때 BA = 0이라 **원본 모델 그대로**에서 출발
- `lora_alpha`는 학습률이 아니라 **adapter 출력의 세기(α/r)**
- r이 크다고 무조건 좋은 거 아님 (과적합·메모리 ↑) → 작게 시작
- **Full FT 메모리** (파라미터 1개당): 가중치 4B + Gradient 4B + Adam 8B + Activation
- **QLoRA** = 4비트로 얼린 베이스 모델 + 16비트 LoRA Adapter만 학습
- **RAG vs Fine-tuning**: "**알아야** 하는가(RAG) / **할 줄 알아야** 하는가(Fine-tuning)"
  - Fine-tuning은 **형식·말투**를 가르침, **지식**은 잘 안 들어감 (실습: 형식 100%, 정답 5%)
  - 순서: **프롬프팅 → RAG → Fine-tuning**

---

## 12. 양자화 Quantization (`05-2`)

### 12-1. 양자화 수식 (계산 문제 가능) ⭐⭐⭐
```python
levels = 2**bits - 1                         # INT8: 255, INT4: 15
scale = (x_max - x_min) / levels             # 한 칸의 간격
zero_point = round(-x_min / scale)           # 실수 0이 어느 정수로 가는지
q  = torch.round(x / scale) + zero_point     # 양자화 (실수 → 정수)
x_ = (q - zero_point) * scale                # 역양자화 (정수 → 실수, 원본과 약간 다름)
```
- 오차의 원인 = **`round()` 반올림**. 비트가 적을수록(단계가 적을수록) 오차 ↑

### 12-2. 정밀도별 메모리 (계산 문제 단골) ⭐⭐⭐
| 정밀도 | 파라미터 1개당 | 1B 모델 | FP32 대비 |
|---|---|---|---|
| FP32 | 4바이트 | 4GB | - |
| FP16 | 2바이트 | 2GB | 50% ↓ |
| INT8 | 1바이트 | 1GB | 75% ↓ |
| INT4 | 0.5바이트 | 0.5GB | 87.5% ↓ |
```python
memory_GB = total_params * 바이트 / 1024**3
```

### 12-3. 4비트 모델 로딩 (BitsAndBytesConfig) ⭐⭐⭐
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# 기준선: FP16
model_fp16 = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, device_map='auto')

# INT4
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                       # ① 4비트로 저장
    bnb_4bit_quant_type='nf4',               # ② NF4 방식 (정규분포 맞춤)
    bnb_4bit_compute_dtype=torch.float16,    # ③ 계산은 FP16으로 풀어서
    bnb_4bit_use_double_quant=True,          # ④ scale 같은 상수도 한 번 더 압축
)
model_int4 = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config,
                                                  device_map='auto')

del model_fp16; torch.cuda.empty_cache()     # GPU 메모리 비우기
```

### 12-4. 양자화 이론 ⭐⭐
- **NF4**: LLM 가중치는 0 근처에 몰린 **정규분포** → 0 근처에 단계를 촘촘하게 배치 → 같은 4비트로 오차 ↓
- **PTQ**: 학습 끝난 모델을 나중에 압축 (재학습 X, 간편) / **QAT**: 양자화를 고려하며 학습
- **QLoRA**는 둘 다 아님: 양자화된 모델은 얼리고 Adapter만 학습
- **양자화는 가중치만 압축** → 활성화값·KV 캐시는 그대로라 **피크 메모리 절감은 더 작음**
- **양자화해도 항상 빨라지진 않음** (계산 직전 역양자화 비용)
- 양자화 모델은 오타·구어체 같은 **환경 변화(Distribution Shift)**에 더 약함 → **TTP**(추론 시 프롬프트 강화)로 보완
- TTP로도 **산술 계산**은 못 고침 → Tool(Agent)을 붙여야 함

---

## 🧭 전체 큰 그림 — "LLM이 원하는 대로 안 될 때"

| 문제 | 해법 | 챕터 |
|---|---|:---:|
| 프롬프트가 부실하다 | 프롬프팅 기법 (Few-shot, CoT, Role) | 2-2 |
| 우리 회사 정보를 모른다 | **RAG** — 자료를 검색해서 준다 | 4-1 |
| 외부 도구·계산이 필요하다 | **Agent** — 도구를 쥐여준다 | 4-2 |
| 말투·형식이 안 맞는다 | **Fine-tuning(LoRA)** — 학습시킨다 | 5-1 |
| GPU 메모리가 부족하다 | **Quantization** — 압축한다 | 5-2 |

> 싼 방법부터: **프롬프팅 → RAG → Fine-tuning → 양자화 배포**

---

## ✅ 자주 틀리는 포인트 체크리스트

- [ ] 싸이킷런 X는 `reshape(-1, 1)`로 2차원
- [ ] test 데이터엔 `fit` 하지 말고 `transform`만
- [ ] `roc_auc_score`엔 `predict_proba(...)[:, 1]` 확률을 넣음
- [ ] `optimizer.zero_grad()` 빠뜨리면 기울기 누적
- [ ] `CrossEntropyLoss` 앞에 Softmax 붙이면 안 됨
- [ ] 분류 정답 텐서는 `dtype=torch.long`
- [ ] 추론할 땐 `model.eval()` + `with torch.no_grad():`
- [ ] 토크나이저와 모델은 **같은 이름**으로 불러오기
- [ ] 모델에 넣을 땐 `return_tensors='pt'` + `model(**encoded)`
- [ ] `last_hidden_state` shape = `[배치, 토큰수, 768]`
- [ ] LLM 응답은 문자열 → `json.loads()` 필수
- [ ] strict 스키마: 모든 키 required + `additionalProperties: False`
- [ ] GPT-5 계열은 `temperature` 대신 `reasoning={'effort': ...}`
- [ ] CNN 출력 크기 = 입력 - 커널 + 1, 풀링 ÷ 2 → Linear 입력 크기 맞추기
- [ ] conv1의 out_channels = conv2의 in_channels
- [ ] `torch.flatten(x, 1)` — 배치 차원(0)은 남김
- [ ] 모델 `.to(device)` 했으면 데이터도 `.to(device)`
- [ ] 전이학습: 얼리기 → `model.fc` 교체 → 그다음 옵티마이저 생성
- [ ] 특징 추출이면 옵티마이저에 `model.fc.parameters()`만
- [ ] 사전학습 모델엔 ImageNet 정규화값 `[0.485, 0.456, 0.406] / [0.229, 0.224, 0.225]`
- [ ] 이미지 하나 넣을 땐 `.unsqueeze(0)`으로 배치 차원 추가
- [ ] `chunk_overlap`은 경계에서 문장 잘림 방지용
- [ ] LangGraph 노드는 State 전체가 아니라 **바꿀 필드만** dict로 반환
- [ ] Memory는 같은 `thread_id`여야 기억함
- [ ] `@tool` docstring이 LLM의 판단 근거
- [ ] Reflection 같은 루프엔 반드시 탈출 조건(최대 횟수)
- [ ] LoRA: B는 0으로 초기화, 학습 파라미터 = 2dr
- [ ] `apply_chat_template`: 학습은 `add_generation_prompt=False`, 추론은 `True`
- [ ] 양자화 메모리: FP32 4B / FP16 2B / INT8 1B / INT4 0.5B
