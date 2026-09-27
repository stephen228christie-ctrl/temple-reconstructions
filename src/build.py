"""Build solomons-temple/index.html from the source file and the KJV verse store.
Usage: python3 src/build.py   (run from the repo root)"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root/'src/solomons-temple.src.html').read_text()
kjv = json.loads((root/'src/kjv.json').read_text())
body = src.replace('__KJV__', json.dumps(kjv, ensure_ascii=False).replace('</', '<\\/'))
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>\n'
        '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(root/'solomons-temple/index.html').write_text(html)
(root/'solomons-temple.artifact.html').write_text(body)   # body-only version for publishing as a claude.ai artifact
print('built', len(html), 'bytes')
