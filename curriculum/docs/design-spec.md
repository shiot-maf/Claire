# 워크시트 디자인 규격

한국어 화자 초등학생이 영어로 구조적 글쓰기를 익히는 인쇄용 워크시트의 규격.
새 단계를 만들거나 기존 단계를 고칠 때 이 문서를 따른다.

## 1. 출력 형식

- 단일 HTML 파일. 외부 스크립트·이미지 없음. 폰트만 Google Fonts 링크.
- `<div class="stack">` 안에 `<section class="sheet">`를 나열. **1 sheet = A4 1장.**
- 인쇄 시 sheet마다 페이지 넘김. 화면에서는 카드로 쌓여 보인다.
- 각 sheet 우측 상단에 `<span class="pagemark">N단계 · 3/15</span>`.

## 2. 색 토큰

라이트와 다크를 모두 정의한다. 색은 반드시 토큰으로만 쓰고,
미디어쿼리 안에서 컴포넌트 색을 정의하지 않는다.

```css
:root{
  --sheet:#FFFDF7;  --page:#EFEADC;        /* 종이 / 바탕 */
  --ink:#262A1F;    --ink-soft:#5B5D4C;    /* 본문 / 보조 */
  --accent:#1E6B49; --accent-soft:#E4EFE8; --accent-ink:#F4FBF6;
  --correction:#B23B32; --correction-soft:#F7E4E0;  /* 빨간펜 */
  --border:#D5CDB6; --line:#C6BEA6;        /* 테두리 / 필기선 */
  --mono-ink:#7A7663;
}
:root[data-theme="dark"]{
  --sheet:#20261F;  --page:#161A15;
  --ink:#ECE7D6;    --ink-soft:#B4B19D;
  --accent:#6FC79A; --accent-soft:#22321F; --accent-ink:#0D1611;
  --correction:#E2897C; --correction-soft:#3A2420;
  --border:#3A4034; --line:#454B3D; --mono-ink:#8B9083;
}
```

같은 다크 값을 `@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){...} }`
에도 반복한다.

## 3. 서체

```css
--font-display: 'Noto Serif KR', Georgia, serif             /* 제목 */
--font-read:    'Noto Serif KR', Georgia, serif             /* 영어 지문·문장 틀 */
--font-ui:      'Noto Sans KR', -apple-system, sans-serif   /* 한국어 지시문 */
--font-mono:    'JetBrains Mono', ui-monospace, monospace   /* 라벨·번호 */
```

원칙: **영어 = serif, 한국어 지시문 = sans, 라벨 = mono.** 눈으로 언어가 구분되게 한다.

## 4. 필기 공간

```css
/* 줄 */
.lines{ background-image: repeating-linear-gradient(
  to bottom, transparent 0 32px, var(--line) 32px 33px); }
/* .l1(1줄) .l2 .l3 .l4 .l5 로 높이 지정 */

/* 인라인 빈칸 */
.blank{ display:inline-block; min-width:130px; border-bottom:1.5px solid var(--line); }
/* .short(74px) .long(200px) */
```

네모칸은 1.5px 실선. 순서 배열용 30×30, 체크박스 16×16.

## 5. 필수 컴포넌트

| 클래스 | 쓰임 |
|---|---|
| `.chapbar` | 챕터 머리띠 — `CHAPTER N` 배지 + 제목 + 소재 + **도움 표시(●●●○)** |
| `.passage` | 영어 지문. 왼쪽 3px accent 세로선, `--page` 바탕, line-height 2.05 |
| `.compare` | 지문 2개 좌우 비교 (2단 grid, 640px 이하 1단) |
| `.bank` | 워드뱅크. 기능별 행 (왼쪽 라벨 / 오른쪽 chip 나열) |
| `.topicbox` | 점선 테두리 + accent-soft 바탕. 낱말 선택지 상자 |
| `.plan` | 계획표 (왼쪽 키 / 오른쪽 필기칸 grid) |
| `.rule` | 규칙 카드. 왼쪽 3px correction 세로선 + correction-soft 바탕 |
| `.chapclose` | 챕터 끝 2px accent 테두리 체크리스트 |
| `.tnote` | **「선생님께」** — 점선 테두리, 각 sheet 맨 아래. 정답은 `.ans` |

## 6. 인쇄 규칙

```css
@media print{
  body{background:#fff;}
  .sheet{border:none; padding:0 0 12mm; page-break-after:always;}
  .sheet:last-of-type{page-break-after:auto;}
  .passage, .tnote, .rule, .chip, .topicbox, .chapbar{background:#fff;}
  @page{size:A4; margin:16mm 14mm;}
}
```

## 7. 내용 규칙

디자인만큼 중요하다. 아래 넷은 비영어권 학습자용 설계의 핵심이며,
하나라도 빠지면 그냥 영어 워크시트가 된다.

### 7-1. 4단 흐름 — 모든 챕터가 같은 순서

```
보기 SEE → 나누기 SORT → 채우기 FRAME → 짓기 BUILD
```

**SORT는 영어 산출이 0이어야 한다.** 밑줄·✗표·번호·알파벳 한 글자만.
영어가 약한 학생도 구조 이해도를 온전히 보여줄 수 있는 구간이므로 절대 빼지 않는다.

### 7-2. 4개 챕터 · 도움 체감

한 단계 = 표지 1 + 워드뱅크 1 + 챕터 4×3장 + 완성과제 1 = **15장**
같은 기술을 소재만 바꿔 네 번 반복하고, 챕터마다 도움을 한 칸씩 줄인다.

| | 도움 | 산출 |
|---|---|---|
| CH1 | ●●●● | 빈칸만 채움 (낱말 몇 개) |
| CH2 | ●●●○ | 빈칸 + 짧은 문장 |
| CH3 | ●●○○ | 틀 제공, 학생이 소재 선택 |
| CH4 | ●○○○ | 백지 + 계획표만 |

### 7-3. 지시문 언어 (단계별 전환)

| 단계 | 지시문 |
|---|---|
| 1~2 | 한국어만 |
| 3~4 | 한국어 굵게(주) + 영어 작게(부) |
| 5~6 | 영어 굵게(주) + 한국어 작게(각주) |

지문과 학생 산출은 **항상 영어**. 「선생님께」는 **항상 한국어**.

### 7-4. 반복 소재 6개 — 1~6단계 공통, 바꾸지 않음

```
my pet · our town · my favourite food · a season · a school day · an animal I know
```

단계가 올라가도 어휘를 새로 배우지 않고 구조만 바뀌므로 어휘가 누적된다.
등장인물도 재사용한다 (강아지 Kongi, 고양이 Nabi).

### 7-5. 「선생님께」에 반드시 넣을 것

- 정답 (여러 답이 가능하면 "모두 인정" 명시)
- **무엇을 보지 말아야 하는지** — 대개 철자·문법
- 이 단계의 통과 기준 한 줄
- 학생이 틀리는 지점과 그때 던질 질문

## 8. 하지 말 것

- 한 장에 활동 5개 이상 (한 장 = 10~15분)
- 문법 용어 (초2에게 '명령문' 대신 "내가 한 일 / 네가 할 일")
- 계획 단계를 영어로 강제 (구조 잡기 + 영어 옮기기 동시 요구 = 붕괴)
- 정답이 하나뿐인 열린 활동
- 소리 내어 말하기 단계 생략 (모든 쓰기 앞에 구두 연습을 붙인다)
