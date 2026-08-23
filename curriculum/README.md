# 구조적 글쓰기 커리큘럼

한국어 화자 초등학생이 **영어로 구조적 글쓰기**를 익히는 6단계 커리큘럼과 인쇄용 워크시트.

단계 구성과 각 단원의 확인 기준은 [Marble Skill Taxonomy](https://github.com/withmarbleapp/os-taxonomy)의
Writing Composition 도메인(38개 주제)과 선수학습 관계 3,221개에서 도출했다.
원본 데이터는 [`../data/os-taxonomy/`](../data/os-taxonomy/)에 있다.

## 무엇이 들어 있나

### 지도

| 파일 | 내용 |
|---|---|
| [`blueprint.html`](blueprint.html) | **글쓰기 설계도** — 6단계 전체 지도와 입문 트랙. 어떤 단원이 어떤 순서로 오는지, 그 근거가 무엇인지 |

### 워크시트 — 학생용

모두 A4 인쇄용. 브라우저에서 열어 인쇄하면 한 장씩 떨어진다.

| 파일 | 대상 | 장수 | 목표 |
|---|---|---|---|
| [`worksheets/entry-1-first-steps.html`](worksheets/entry-1-first-steps.html) | 입문 | 9 | 글쓰기 첫걸음 — 구조를 **한국어로** 먼저 |
| [`worksheets/entry-2-write-it-in-english.html`](worksheets/entry-2-write-it-in-english.html) | 입문 | 7 | 같은 내용을 **영어로** 다시 |
| [`worksheets/stage-1-speaking-to-writing.html`](worksheets/stage-1-speaking-to-writing.html) | 초1 | 7 | 말에서 글로 — 영어 세 문장 |
| [`worksheets/stage-2-purpose.html`](worksheets/stage-2-purpose.html) | 초2 | 15 | 목적을 가진 글 — 같은 일을 두 모양으로 |
| [`worksheets/stage-3-paragraph.html`](worksheets/stage-3-paragraph.html) ★ | 초3 | 15 | 문단의 발견 — 한 문단 = 한 생각 |
| [`worksheets/stage-4-language-of-writing.html`](worksheets/stage-4-language-of-writing.html) | 초4 | 9 | 글쓰기의 언어 — 세 문단, 하나의 흐름 |
| [`worksheets/stage-5-reader-and-reason.html`](worksheets/stage-5-reader-and-reason.html) | 초5 | 9 | 독자와 근거 — 설득하는 글 |
| [`worksheets/stage-6-long-texts.html`](worksheets/stage-6-long-texts.html) | 초6 | 9 | 긴 글 다루기 — 줄이고 구조화하기 |

★ **3단계가 전환점.** 여기서 문장이 문단으로 묶이지 않으면 이후가 모두 무너진다.

### 워크시트 — 교사용

| 파일 | 내용 |
|---|---|
| [`worksheets/teacher-notebook.html`](worksheets/teacher-notebook.html) | **수업 운영 노트** (9장) — 2·3단계 차시 계획표, 학생별 진단표, 반 전체 기록, 처방표 |

### 문서

| 파일 | 내용 |
|---|---|
| [`docs/plan.md`](docs/plan.md) | 기획서 — 왜 이렇게 설계했는지, 이중 진행과 4단 흐름 |
| [`docs/design-spec.md`](docs/design-spec.md) | 디자인 규격 — 색·서체·컴포넌트·인쇄 규칙, 그리고 내용 규칙 |

## 설계의 핵심 네 가지

새 단계를 만들거나 기존 것을 고칠 때 이 넷은 지켜야 한다.
자세한 내용은 [`docs/design-spec.md`](docs/design-spec.md) 7절.

**1. 두 부하를 분리한다.** 구조를 이해하는 능력이 영어 산출 능력보다 항상 앞서간다.
구조는 한국어로 이해하고, 산출만 영어로 한다.

**2. SORT 구간은 영어 산출이 0이다.** 밑줄·✗표·번호만 쓴다.
영어가 약한 학생도 구조 이해도를 온전히 보여줄 수 있는 유일한 구간이라 절대 빼지 않는다.

**3. 같은 기술을 네 번, 도움을 줄여 가며.** 한 단계는 4개 챕터로 같은 기술을
소재만 바꿔 반복하고, 챕터마다 비계를 한 칸씩 걷어낸다(`●●●● → ●○○○`).

**4. 소재 6개를 6단계 내내 돌려 쓴다.**
`my pet · our town · my favourite food · a season · a school day · an animal I know`
단계가 올라가도 어휘를 새로 배우지 않으므로 어휘가 누적된다.

## 진행 순서

```
글쓰기 첫걸음 (한국어)  →  Write It in English  →  1단계 → 2단계 → 3단계 ★ → 4단계 → 5단계 → 6단계
```

입문 트랙 두 권을 마친 학생 중 세 문단을 무리 없이 쓴다면 3단계로 바로 가도 된다.

## 인쇄

각 HTML을 브라우저에서 열고 인쇄(Ctrl/Cmd+P). A4 세로, 여백 기본값.
`<section class="sheet">` 하나가 A4 한 장으로 떨어진다.

## 라이선스

워크시트의 지문과 활동은 이 커리큘럼을 위해 새로 쓴 것이다.
단계 구성과 확인 기준이 근거한 Marble Skill Taxonomy의 표기는 다음과 같다.

> Marble Skill Taxonomy (v1) · © Generative Spark, Inc. (Marble) · https://withmarble.com
> licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content)
