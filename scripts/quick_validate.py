from pathlib import Path
import json
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "SKILL.md",
    "templates/intent-template.md",
    "templates/workflow-template.yaml",
    "templates/output-template.md",
    "templates/result-template.json",
    "references/validation-checklist.md",
    "references/design-notes.md",
]
SECRET_PATTERNS = [
    r"gho_[A-Za-z0-9_]+",
    r"github_pat_[A-Za-z0-9_]+",
    r"api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]+",
    r"password\s*[:=]\s*[A-Za-z0-9_\-]+",
    r"token\s*[:=]\s*[A-Za-z0-9_\-]+",
    r"webhook\s*[:=]\s*https?://",
]


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


for rel in REQUIRED:
    if not (ROOT / rel).exists():
        fail(f"missing required file: {rel}")

for example in (ROOT / "examples").iterdir():
    if example.is_dir():
        for name in ["intent.md", "workflow.yaml", "output.md", "result.json"]:
            if not (example / name).exists():
                fail(f"missing {name} in {example.relative_to(ROOT)}")

for path in ROOT.rglob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))

for path in ROOT.rglob("*.yaml"):
    yaml.safe_load(path.read_text(encoding="utf-8"))

for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                fail(f"possible secret pattern in {path.relative_to(ROOT)}")

print("OK: required files, examples, JSON, YAML, and secret-pattern checks passed")
