# 구조적 글쓰기 커리큘럼

한국어 화자 초등학생이 **영어로 구조적 글쓰기**를 익히는 6단계 커리큘럼과 인쇄용 워크시트.

단계 구성과 각 단원의 확인 기준은 [Marble Skill Taxonomy](https://github.com/withmarbleapp/os-taxonomy)의
Writing Composition 도메인(38개 주제)과 선수학습 관계 3,221개에서 도출했다.
원본 데이터는 [`../data/os-taxonomy/`](../data/os-taxonomy/)에 있다.

## 무엇이 들어 있나

### 지도

| 파일 | 내용 |
|---|---|
| [`blueprint.html`](blueprint.html) | **글쓰기 설계도** — 6단계 전체 지도와 입문 트랙 |

### 워크시트

한 파일이 **교사용과 학생용을 겸한다.** 화면 위쪽의 「선생님께」 토글을 끄면
정답과 지도 요령이 사라지고 그대로 학생용이 된다. **쪽 구성은 바뀌지 않으므로**
“7쪽을 펴세요”가 두 벌에서 같은 쪽을 가리킨다.

| 워크시트 | 대상 | 장수 | 학생이 쓸 소재 |
|---|---|---:|---|
| [`entry-1-first-steps.html`](worksheets/entry-1-first-steps.html) | 입문 | 11 | — (한국어) |
| [`entry-2-write-it-in-english.html`](worksheets/entry-2-write-it-in-english.html) | 입문 | 9 | 내가 잘 아는 것 하나 |
| [`stage-1-speaking-to-writing.html`](worksheets/stage-1-speaking-to-writing.html) | 1단계 | 7 | 여섯 소재 중 하나 |
| [`stage-2-purpose.html`](worksheets/stage-2-purpose.html) | 2단계 | 15 | 내가 만들 줄 아는 음식 |
| [`stage-3-paragraph.html`](worksheets/stage-3-paragraph.html) ★ | 3단계 | 18 | 내가 아는 동물 |
| [`stage-4-language-of-writing.html`](worksheets/stage-4-language-of-writing.html) | 4단계 | 11 | 우리 동네 |
| [`stage-5-reader-and-reason.html`](worksheets/stage-5-reader-and-reason.html) | 5단계 | 12 | 점심시간을 늘리자 |
| [`stage-6-long-texts.html`](worksheets/stage-6-long-texts.html) | 6단계 | 12 | 내가 아는 동물 |
| [`teacher-notebook.html`](worksheets/teacher-notebook.html) | 교사 | 9 | 차시 계획·진단·처방 |

★ **3단계가 전환점.** 여기서 문장이 문단으로 묶이지 않으면 이후가 모두 무너진다.

전 쪽이 **A4 한 장에 정확히** 들어간다 (794×1123px 고정 판형).
「선생님께」를 켠 상태와 끈 상태 **둘 다** 헤드리스 브라우저로 재서 확인했다.

### 워크시트를 고칠 때

```
src/<이름>.html   본문만 (표지·활동·「선생님께」)
_base.css         디자인 전체 — 색·서체·컴포넌트
build.py          두 개를 합쳐 <이름>.html 을 만든다
```

워크시트는 서버 없이 파일 하나로 열려야 하므로 CSS를 파일마다 심어 넣는다.
디자인을 고칠 때는 `_base.css` 하나만 고치고 `python3 build.py`를 돌린다.

쪽이 A4를 넘는지는 눈으로 가늠하지 말고 **재서 확인한다.**
헤드리스 브라우저로 각 `.page`의 자연 높이를 재어 1123px과 견주면 된다.

### 지난 판 — `worksheets/superseded/`

교사용과 학생용을 **별도 파일**로 냈던 이전 판이다. 두 벌의 쪽 번호가 어긋나는
문제가 있어 토글 방식으로 대체했다. 참고용으로만 남겨 두었고, 수업에는 쓰지 않는다.

### 문서

| 파일 | 내용 |
|---|---|
| [`docs/plan.md`](docs/plan.md) | 기획서 — 이중 진행과 4단 흐름 |
| [`docs/design-spec.md`](docs/design-spec.md) | 디자인 규격 — 판형·색·서체·컴포넌트, 내용 규칙 |

## 설계의 핵심 다섯 가지

새 단계를 만들거나 기존 것을 고칠 때 이 다섯은 지켜야 한다.
자세한 내용은 [`docs/design-spec.md`](docs/design-spec.md) 7절.

**1. 두 부하를 분리한다.** 구조를 이해하는 능력이 영어 산출 능력보다 항상 앞서간다.
구조는 한국어로 이해하고, 산출만 영어로 한다.

**2. SORT 구간은 영어 산출이 0이다.** 밑줄·✗표·번호만 쓴다.
영어가 약한 학생도 구조 이해도를 온전히 보여 줄 수 있는 유일한 구간이라 절대 빼지 않는다.

**3. 같은 기술을 네 번, 도움을 줄여 가며.** 한 단계는 4개 챕터로 같은 기술을
소재만 바꿔 반복하고, 챕터마다 비계를 한 칸씩 걷어낸다(`●●●● → ●○○○`).

**4. 학생이 쓸 소재는 하나로 고정한다.** 여럿 중 고르게 하면 반 전체가 제각각이 되어
모델링도 상호 도움도 안 된다. 학생 소재는 대체로 **본보기 글과 다른 것**으로 잡아
베끼지 못하게 한다.

**5. 정답은 「선생님께」 안에만 둔다.** 토글을 끄면 사라진다. 학생에게 인쇄하기 전에
토글이 꺼져 있는지 확인한다.

## 진행 순서

```
글쓰기 첫걸음 (한국어)  →  Write It in English  →  1단계 → 2단계 → 3단계 ★ → 4단계 → 5단계 → 6단계
```

입문 트랙 두 권을 마친 학생 중 세 문단을 무리 없이 쓴다면 3단계로 바로 가도 된다.

## 인쇄

각 HTML을 브라우저에서 열고 **「선생님께」 토글을 끈 다음** 인쇄(Ctrl/Cmd+P).
A4 세로, **여백 없음**, 배경 그래픽 켜기. `<section class="page">` 하나가 A4 한 장이다.

## 라이선스

워크시트의 지문과 활동은 이 커리큘럼을 위해 새로 쓴 것이다.
단계 구성과 확인 기준이 근거한 Marble Skill Taxonomy의 표기는 다음과 같다.

> Marble Skill Taxonomy (v1) · © Generative Spark, Inc. (Marble) · https://withmarble.com
> licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content)
