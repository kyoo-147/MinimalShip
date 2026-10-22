#!/usr/bin/env python3
"""Validate the public MinimalShip bundle without third-party dependencies."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".mjs", ".txt"}
REMOVED_PATHS = {
    "README.vi.md",
    "references/complete-line-index.md",
    "references/yc-comprehensive.vi.md",
    "references/yc-principles.md",
    "sources",
}
REQUIRED_ROOT_MARKERS = (
    "READ",
    "UNDERSTAND",
    "CLARIFY",
    "FEATURES",
    "SPEC",
    "APPROVE",
    "Behavioral evidence",
    "PLAN",
    "DISPATCH",
    "BUILD",
    "VERIFY",
    "SHIP",
    "ITERATE",
    "FEATURES.md",
    "RUN.md",
    "PASS",
    "FAIL",
    "BLOCKED",
    "PROFILE GATE",
    "PROFILE_INCOMPLETE",
    "PROFILE_OPTIONAL",
    "neutral defaults",
)
REQUIRED_REFERENCES = (
    "references/grilling.md",
    "references/orchestration.md",
    "references/product-principles.md",
    "references/distribution.md",
    "references/profile.md",
    "references/stack-routing.md",
)
REQUIRED_ROUTING_MARKERS = (
    "Cloudflare",
    "Expo/EAS",
    "Vercel Agent Skills",
    "auto-install",
    "vendor",
    "Existing configuration",
    "loading, empty, error",
    "device/emulator",
    "rendered behavior",
    "accessibility",
    "performance",
    "BLOCKED",
)
REQUIRED_TEMPLATES = (
    "templates/FEATURES.md",
    "templates/RUN.md",
    "templates/SPEC.md",
    "templates/ADR.md",
)
REQUIRED_PROFILE_TEMPLATES = (
    "templates/profile/PROFILE.md",
    "templates/profile/PROFILE-QUESTIONS.md",
    "templates/profile/VOICE.md",
    "templates/profile/OPINIONS.md",
    "templates/profile/BUILD_PLAYBOOK.md",
    "templates/profile/TASTE_UI.md",
    "templates/profile/RESEARCH_TASTE.md",
    "templates/profile/UI_TESTING.md",
    "templates/profile/ORCHESTRATION.md",
    "templates/profile/PERMISSIONS.md",
)


def fail(message: str) -> NoReturn:
    raise SystemExit(f"FAIL: {message}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")


def load_json(path: Path) -> dict:
    try:
        value = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected an object in {path}")
    return value


def frontmatter(path: Path) -> dict[str, str]:
    lines = read_text(path).splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{path} must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(f"{path} has an unterminated YAML frontmatter block")
    result: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path} has an unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def git_files(root: Path) -> set[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def validate_root(root: Path) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        fail("missing root SKILL.md")
    fm = frontmatter(skill_path)
    if fm.get("name") != "minimalship":
        fail("root SKILL.md must declare name: minimalship")
    if not fm.get("description"):
        fail("root SKILL.md is missing a description")
    root_text = read_text(skill_path)
    missing = [marker for marker in REQUIRED_ROOT_MARKERS if marker not in root_text]
    if missing:
        fail(f"root SKILL.md is missing workflow markers: {', '.join(missing)}")
    for relative in (*REQUIRED_REFERENCES, *REQUIRED_TEMPLATES, *REQUIRED_PROFILE_TEMPLATES):
        if not (root / relative).is_file():
            fail(f"missing required public artifact: {relative}")
    for helper in (
        "scripts/init-profile.py",
        "scripts/profile-status.py",
        "scripts/smoke-install.py",
        "scripts/smoke-links.sh",
        "scripts/smoke-profile.py",
        "scripts/smoke-workflow.py",
        "scripts/grade-evals.py",
        "scripts/run-evals.py",
        "scripts/route-stack.py",
        "scripts/smoke-runtime.py",
    ):
        if not (root / helper).is_file():
            fail(f"missing validation helper: {helper}")
    profile_questions = read_text(root / "templates/profile/PROFILE-QUESTIONS.md")
    missing_profile_groups = [f"P{index:02d}." for index in range(1, 11) if f"P{index:02d}." not in profile_questions]
    if missing_profile_groups:
        fail(f"profile question catalog is missing groups: {', '.join(missing_profile_groups)}")


def validate_evals(root: Path) -> None:
    scenarios_path = root / "evals" / "scenarios.json"
    data = load_json(scenarios_path)
    expected = [f"E{index:02d}" for index in range(1, 9)]
    if data.get("schema_version") != 1 or data.get("scenario_ids") != expected:
        fail("evals/scenarios.json must declare schema_version 1 and scenario_ids E01-E08")
    if not (root / "evals" / "README.md").is_file():
        fail("missing evals/README.md")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or [item.get("id") for item in scenarios if isinstance(item, dict)] != expected:
        fail("evals/scenarios.json must contain exactly E01-E08 in order")
    required = {"title", "prompt", "input", "expected_behavior", "failure_modes", "required_evidence", "baseline_comparison", "runtime_requirements"}
    for item in scenarios:
        if not isinstance(item, dict) or not required.issubset(item):
            fail(f"eval scenario is missing required fields: {item}")
        sid = item["id"]
        fixture = root / "evals" / "fixtures" / sid / "input.json"
        if not fixture.is_file():
            fail(f"missing behavioral fixture: {fixture.relative_to(root)}")
        fixture_data = load_json(fixture)
        if fixture_data.get("fixture") != sid:
            fail(f"behavioral fixture {sid} does not identify itself")


def validate_routing(root: Path) -> None:
    reference = read_text(root / "references/stack-routing.md")
    missing = [marker for marker in REQUIRED_ROUTING_MARKERS if marker not in reference]
    if missing:
        fail(f"stack-routing reference is missing markers: {', '.join(missing)}")
    forbidden = (r"\bnpx\s+skills\s+add\b", r"\bnpm\s+install\b", r"\byarn\s+add\b", r"\bpnpm\s+add\b", r"\beas\s+build\b", r"\bwrangler\s+deploy\b", r"\bvercel\s+deploy\b")
    found = [pattern for pattern in forbidden if re.search(pattern, reference, flags=re.IGNORECASE)]
    if found:
        fail(f"stack-routing reference contains executable side-effect commands: {', '.join(found)}")
    route_script = root / "scripts/route-stack.py"
    if not route_script.is_file():
        fail("missing stack-routing detector: scripts/route-stack.py")


def validate_skill(root: Path, bucket: str, skill_dir: Path, root_readme: str, plugin_skills: set[str]) -> None:
    name = skill_dir.name
    skill_path = skill_dir / "SKILL.md"
    metadata_path = skill_dir / "agents" / "openai.yaml"
    handbook_path = root / "handbook" / bucket / f"{name}.md"
    if not skill_path.is_file() or not metadata_path.is_file():
        fail(f"{bucket}/{name} needs SKILL.md and agents/openai.yaml")
    fm = frontmatter(skill_path)
    if fm.get("name") != name or not fm.get("description"):
        fail(f"{skill_path} has invalid name or description metadata")
    metadata = read_text(metadata_path)
    if "interface:" not in metadata or "display_name:" not in metadata or "short_description:" not in metadata:
        fail(f"{metadata_path} is missing interface metadata")
    explicit = "disable-model-invocation: true" in skill_path.read_text(encoding="utf-8")
    implicit_blocked = "allow_implicit_invocation: false" in metadata
    if explicit != implicit_blocked:
        fail(f"invocation policy mismatch for {skill_path}")
    if not handbook_path.is_file():
        fail(f"missing handbook page: {handbook_path.relative_to(root)}")
    expected_link = f"skills/{bucket}/{name}/SKILL.md"
    bucket_link = f"./{name}/SKILL.md"
    bucket_readme = read_text(root / "skills" / bucket / "README.md")
    if bucket_link not in bucket_readme or expected_link not in root_readme:
        fail(f"{expected_link} is missing from a README index")
    if f"./skills/{bucket}/{name}" not in plugin_skills:
        fail(f"{expected_link} is missing from .claude-plugin/plugin.json")


def validate_public_content(root: Path, tracked: set[str]) -> None:
    for removed in REMOVED_PATHS:
        if (root / removed).exists():
            fail(f"removed path still exists: {removed}")
    for path in tracked:
        if path.startswith(("docs/", "analysis/", ".local/")):
            fail(f"local-only path is tracked: {path}")
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in {".git", "docs", "analysis", ".local", ".pi", ".minimalship", "scripts"} for part in relative.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8")
            if "Pasted text" in text or "complete-line-index" in text or "yc-comprehensive" in text:
                fail(f"raw or removed-source marker remains in {relative}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    validate_root(root)
    validate_evals(root)
    validate_routing(root)
    tracked = git_files(root)
    validate_public_content(root, tracked)

    package = load_json(root / "package.json")
    plugin = load_json(root / ".claude-plugin" / "plugin.json")
    if package.get("version") != plugin.get("version"):
        fail("package.json and .claude-plugin/plugin.json versions differ")
    if plugin.get("name") != "minimalship-skills":
        fail("plugin.json has the wrong package name")
    plugin_skills = set(plugin.get("skills", []))
    root_readme = read_text(root / "README.md")
    found: list[str] = []
    for bucket in ("engineering", "productivity"):
        bucket_dir = root / "skills" / bucket
        if not bucket_dir.is_dir():
            fail(f"missing promoted skill bucket: {bucket}")
        for skill_dir in sorted(path for path in bucket_dir.iterdir() if path.is_dir()):
            validate_skill(root, bucket, skill_dir, root_readme, plugin_skills)
            found.append(f"./skills/{bucket}/{skill_dir.name}")
    if set(found) != plugin_skills:
        fail("plugin.json skills list does not match the promoted skill tree")
    for bucket in ("misc", "in-progress", "deprecated"):
        if not (root / "skills" / bucket / "README.md").is_file():
            fail(f"missing structural bucket README: {bucket}")
    root_agent = read_text(root / "agents" / "openai.yaml")
    if "display_name:" not in root_agent or "allow_implicit_invocation: false" not in root_agent:
        fail("root agents/openai.yaml has invalid metadata")

    print(f"PASS: MinimalShip bundle validated: {len(found)} promoted skills, {len(REQUIRED_REFERENCES)} references, {len(REQUIRED_TEMPLATES)} templates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
