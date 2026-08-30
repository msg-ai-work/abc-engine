#!/usr/bin/env python3
"""Validate Top 3 Domain Skill/Eval structure.

This runner does not call an LLM. It protects the repository contract so that
human/Kiro evaluation can run against complete, versioned inputs.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TOP3 = ROOT / "skills" / "TOP3.md"


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)
    print(f"::error::{message}")


def parse_top3(text: str) -> list[str]:
    skills = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        match = re.search(r"`([a-z0-9-]+)`", line)
        if match:
            name = match.group(1)
            if name not in skills:
                skills.append(name)
    return skills[:3]


def parse_version(text: str) -> tuple[int, int]:
    match = re.search(r'^version:\s*["\']?([0-9]+)\.([0-9]+)', text, re.MULTILINE)
    if not match:
        return (-1, -1)
    return int(match.group(1)), int(match.group(2))


def main() -> int:
    errors: list[str] = []

    if not TOP3.exists():
        fail("skills/TOP3.md is required", errors)
        return 1

    top_skills = parse_top3(TOP3.read_text(encoding="utf-8"))
    if len(top_skills) != 3:
        fail(f"TOP3.md must define exactly 3 skills; found {len(top_skills)}: {top_skills}", errors)

    for skill in top_skills:
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        eval_file = ROOT / "evals" / skill / "EVAL.md"

        if not skill_file.exists():
            fail(f"missing Skill: skills/{skill}/SKILL.md", errors)
            continue
        if not eval_file.exists():
            fail(f"missing Eval: evals/{skill}/EVAL.md", errors)
            continue

        skill_text = skill_file.read_text(encoding="utf-8")
        eval_text = eval_file.read_text(encoding="utf-8")

        version = parse_version(skill_text)
        if version < (0, 2):
            fail(f"{skill}: Top3 Skill version must be >= 0.2; found {version}", errors)

        if "priority: top-3" not in skill_text:
            fail(f"{skill}: frontmatter must contain 'priority: top-3'", errors)

        required_skill_sections = ["## 입력", "## 절차", "## 출력"]
        for section in required_skill_sections:
            if section not in skill_text:
                fail(f"{skill}: missing required Skill section '{section}'", errors)

        eval_lower = eval_text.lower()
        for marker in ["case 1", "case 2", "expected result"]:
            if marker not in eval_lower:
                fail(f"{skill}: EVAL.md missing '{marker}'", errors)

        if "fail conditions" not in eval_lower and "hard fail" not in eval_lower:
            fail(f"{skill}: EVAL.md must define Fail Conditions or Hard Fail", errors)

        dangerous_literals = ["-----BEGIN PRIVATE KEY-----", "AKIAIOSFODNN7EXAMPLE"]
        for literal in dangerous_literals:
            if literal in skill_text or literal in eval_text:
                fail(f"{skill}: possible secret/private key material detected", errors)

        print(f"OK {skill}: version {version[0]}.{version[1]}, Skill + 2 Eval Cases")

    if errors:
        print(f"\nFAILED: {len(errors)} contract error(s)")
        return 1

    print(f"\nPASS: validated {len(top_skills)} Top3 skills and their eval contracts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
