#!/usr/bin/env python3
"""Check required artifacts and all original files against the SHA256 manifest."""
from pathlib import Path
import json,hashlib,sys
r=Path(__file__).resolve().parents[1]
assert (r/'SKILL.md').is_file() and (r/'templates/RUN.md').is_file()
s=(r/'SKILL.md').read_text()
assert s.startswith('---\nname: minflow\n') and 'ASK' in s and 'DISPATCH' in s and 'VERIFY' in s
manifest=json.loads((r/'sources/SHA256.json').read_text())
for name,expected in manifest.items():
 b=(r/'sources'/name).read_bytes(); digest=hashlib.sha256(b).hexdigest(); assert digest==expected, name
idx=(r/'references/complete-line-index.md').read_text(encoding='utf-8')
for name in manifest:
 lines=(r/'sources'/name).read_text(encoding='utf-8-sig').splitlines()
 assert f'SOURCE: {name} (' in idx
 assert f'[{len(lines):04d}]' in idx, name
print('PASS: skill structure and all original bytes/line counts verified:',len(manifest),'unique sources')
