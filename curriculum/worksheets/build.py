#!/usr/bin/env python3
"""워크시트 조립기.

src/<이름>.html (본문) + _base.css (공통 디자인) → <이름>.html (단일 파일).

워크시트는 외부 파일 없이 혼자 열려야 하므로 CSS를 파일마다 심어 넣는다.
디자인을 고칠 때는 _base.css 하나만 고치고 이 스크립트를 다시 돌린다.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).parent
PAGE = '<section class="page'
CSS = (HERE / "_base.css").read_text(encoding="utf-8").rstrip()

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


def build(src):
    text = src.read_text(encoding="utf-8")
    match = re.match(r"<!--title:\s*(.+?)\s*-->\s*", text)
    if not match:
        raise SystemExit(f"{src.name}: 첫 줄에 <!--title: ...--> 가 있어야 한다")
    out = HERE / src.name
    out.write_text(
        HEAD.format(title=match.group(1), css=CSS, body=text[match.end():].rstrip()),
        encoding="utf-8",
    )
    pages = out.read_text(encoding="utf-8").count(PAGE)
    print(f"{out.name}  {pages}쪽")


for path in sorted((HERE / "src").glob("*.html")):
    build(path)
