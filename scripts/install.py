#!/usr/bin/env python3
"""Non-destructive MINFLOW installer. No external downloads or executable hooks."""
import argparse, shutil
from pathlib import Path
p=argparse.ArgumentParser()
g=p.add_mutually_exclusive_group(required=True)
g.add_argument('--global',dest='global_install',action='store_true',help='Install into ~/.pi/agent/skills/minflow')
g.add_argument('--project',type=Path,help='Project directory into which .pi/skills/minflow is installed')
p.add_argument('--force',action='store_true',help='Replace existing MINFLOW skill')
a=p.parse_args()
src=Path(__file__).resolve().parents[1]
assert (src/'SKILL.md').is_file()
dest=(Path.home()/'.pi/agent/skills/minflow') if a.global_install else (a.project.expanduser().resolve()/'.pi/skills/minflow')
if src.resolve()==dest.resolve():
 print('Already installed:',dest)
 raise SystemExit(0)
if dest.exists():
 if not a.force: raise SystemExit(f'Existing skill at {dest}; pass --force to replace deliberately')
 if dest.is_dir():shutil.rmtree(dest)
 else:dest.unlink()
dest.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(src,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.DS_Store'))
print('Installed:',dest)
print('Open Pi and run /skill:minflow <task>')
