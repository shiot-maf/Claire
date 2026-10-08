#!/usr/bin/env python3
"""색 팔레트 문서를 tokens.css 에서 다시 만든다.

    python3 design/make-palette.py   →  docs/palette.html

색을 고쳤으면 이 스크립트를 돌려 팔레트를 맞춰 둔다. 대비와 회색값은
tokens.css 를 읽어 계산하므로, 손으로 적은 숫자가 틀어질 일이 없다.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).parent
CSS = (HERE / "tokens.css").read_text(encoding="utf-8")
OUT = HERE.parent / "docs" / "palette.html"

NAMES = {'1': ('빨강', '말에서 글로'), '2': ('주황', '목적을 가진 글'),
         '3': ('겨자', '문단의 발견'), '4': ('초록', '글쓰기의 언어'),
         '5': ('파랑', '독자와 근거'), '6': ('남색', '긴 글 다루기')}


def lum(hx):
    hx = hx.lstrip('#')
    c = [int(hx[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + .05) / (lo + .05)


def grey(hx):
    v = round(lum(hx) ** (1 / 2.2) * 255)
    return '#%02X%02X%02X' % (v, v, v), v


ST, CH = {}, {}
for m in re.finditer(r'\[data-st="(\d)"\]\{--st:(#\w{6}); --st-on:(#\w{6}); '
                     r'--st-soft:(#\w{6}); --st-deep:(#\w{6});\}', CSS):
    ST[m.group(1)] = m.groups()[1:]
for m in re.finditer(r'\[data-st="(\d)"\] \[data-ch="(\d)"\]\{--ch:(#\w{6}); --ch-on:(#\w{6}); '
                     r'--ch-soft:(#\w{6}); --ch-deep:(#\w{6});\}', CSS):
    CH.setdefault(m.group(1), {})[m.group(2)] = m.groups()[2:]

cards = []
for i in '123456':
    hue, title = NAMES[i]
    c, on, soft, deep = ST[i]
    g, gv = grey(c)
    cards.append(f'''<article class="scard" style="--c:{c};--on:{on};--s:{soft};--d:{deep};">
  <header><span class="num">{i}</span><div><h3>{hue}</h3><p>{i}단계 · {title}</p></div></header>
  <div class="ramp">
    <div class="sw main"><b>{c}</b><span>배지 · 머리띠</span></div>
    <div class="sw soft"><b>{soft}</b><span>상자 바탕</span></div>
    <div class="sw deep"><b>{deep}</b><span>글자</span></div>
  </div>
  <div class="meta"><span class="gchip" style="background:{g};color:{'#2A2622' if gv > 140 else '#fff'}">{gv}</span>
    <span>흑백으로 바꾸면 <b>{g}</b></span><span class="c">대비 {max(contrast(c, "#FFFFFF"), contrast(c, "#2A2622")):.1f}</span></div>
</article>''')

rows = []
for i in '123456':
    cells = ''.join(
        f'<div class="cell" style="--c:{CH[i][j][0]};--on:{CH[i][j][1]};--s:{CH[i][j][2]};">'
        f'<div class="badge">CH{j}</div><div class="tint"></div>'
        f'<b>{CH[i][j][0]}</b><span>{grey(CH[i][j][0])[1]}</span></div>' for j in '1234')
    rows.append(f'<div class="chrow"><div class="rl"><b>{i}단계</b>'
                f'<span>{NAMES[i][0]}</span></div>{cells}</div>')

mocks = []
for i, j, pill, h in [('2', '1', '보기 SEE', '같은 일, 두 모양'),
                      ('2', '4', '짓기 BUILD', '두 모양으로 쓰기'),
                      ('6', '1', '보기 SEE', '긴 글과 줄인 글'),
                      ('6', '4', '짓기 BUILD', '소제목과 표')]:
    c, on, soft, deep = CH[i][j]
    dots = ('<i class="on"></i>' * (5 - int(j))) + ('<i></i>' * (int(j) - 1))
    mocks.append(f'''<div class="mock" style="--c:{c};--on:{on};--s:{soft};--d:{deep};">
  <div class="bar"><span class="bg">CHAPTER {j}</span><span class="nm">{i}단계 · {NAMES[i][0]}</span><span class="help">{dots}</span></div>
  <div class="hd"><span class="pill">{pill}</span><h4>{h}</h4></div>
  <p class="lab">활동 1</p><p class="q">빈칸에 알맞은 말을 골라 쓰세요.</p>
  <div class="chips"><span>First,</span><span>Next,</span><span>Finally,</span></div>
  <div class="tip">막히면 앞 쪽을 보세요. 그대로 옮겨 써도 좋습니다.</div>
</div>''')

greys = [(i, ST[i][0], *grey(ST[i][0])) for i in '123456']
ladder = ''.join(f'<div class="lstep" style="--c:{c};"><b>{i}</b><i></i><span>{gv}</span></div>'
                 for i, c, g, gv in greys)
mingap = min(abs(a[3] - b[3]) for k, a in enumerate(greys) for b in greys[k + 1:])

TEMPLATE = (HERE / "palette.template.html").read_text(encoding="utf-8")
OUT.write_text(TEMPLATE
               .replace('<!--CARDS-->', '\n'.join(cards))
               .replace('<!--LADDER-->', ladder)
               .replace('<!--CHROWS-->', '\n'.join(rows))
               .replace('<!--MOCKS-->', '\n'.join(mocks))
               .replace('MINGAP', str(mingap)), encoding="utf-8")
print(f'{OUT.relative_to(HERE.parent)}  단계 {len(ST) - 1}색 · 최소 회색 간격 {mingap}')
