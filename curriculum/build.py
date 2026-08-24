#!/usr/bin/env python3
"""커리큘럼 문서 조립기.

src/<이름>.html (본문) + design/*.css (디자인) → 단일 HTML 파일.

문서는 서버 없이 파일 하나로 열려야 하므로 CSS를 파일마다 심어 넣는다.
디자인을 고칠 때는 design/ 아래만 고치고 이 스크립트를 다시 돌린다.

본문 첫 줄에 지시자를 둔다.

    <!--title: 문단의 발견-->
    <!--layout: sheet-->      sheet(기본, A4 고정 판형) 또는 map(설계도)
    <!--out: blueprint.html-->  기본값은 worksheets/<이름>.html
"""
import pathlib
import re

HERE = pathlib.Path(__file__).parent
DESIGN = HERE / "design"
PAGE = '<section class="page'

LAYERS = {
    "sheet": ["tokens.css", "sheet.css"],
    "map": ["tokens.css", "map.css"],
}

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Fredoka:wght@400;500;600&family=Noto+Sans+KR:wght@400;500;700&display=swap">
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def directives(text):
    found = {}
    while True:
        match = re.match(r"<!--\s*(title|layout|out)\s*:\s*(.+?)\s*-->\s*", text)
        if not match:
            return found, text
        found[match.group(1)] = match.group(2)
        text = text[match.end():]


def build(src):
    meta, body = directives(src.read_text(encoding="utf-8"))
    if "title" not in meta:
        raise SystemExit(f"{src.name}: 첫 줄에 <!--title: ...--> 가 있어야 한다")
    layout = meta.get("layout", "sheet")
    if layout not in LAYERS:
        raise SystemExit(f"{src.name}: layout 은 {' 또는 '.join(LAYERS)} 여야 한다")

    css = "\n\n".join((DESIGN / name).read_text(encoding="utf-8").rstrip()
                      for name in LAYERS[layout])
    out = HERE / meta.get("out", f"worksheets/{src.name}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HEAD.format(title=meta["title"], css=css, body=body.rstrip()),
                   encoding="utf-8")

    pages = out.read_text(encoding="utf-8").count(PAGE)
    size = f"{pages}쪽" if pages else "한 폭"
    print(f"{out.relative_to(HERE)}  {size}")


for path in sorted((HERE / "src").glob("*.html")):
    build(path)
