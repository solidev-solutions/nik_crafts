"""Compare the repository's own pre-commit checks with the examples in check_fixtures.txt.

Each fixture line names the check that must reject a text, or "ok" when none may. For the
checks that look at file names the text is a path, for the one that looks at file content
it is a line of Python.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = {"[paths]": "fail", "[lines]": "pygrep"}


def rejects(hook: dict, text: str, config: dict) -> bool:
	if hook["language"] == "pygrep":
		return bool(re.search(hook["entry"], text))
	return bool(
		re.search(hook["files"], text)
		and not re.search(hook.get("exclude", "^$"), text)
		and not re.search(config.get("exclude", "^$"), text)
	)


def main() -> int:
	config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
	hooks = [
		hook
		for repo in config["repos"]
		if repo["repo"] == "local"
		for hook in repo["hooks"]
		if hook["language"] in SECTIONS.values()
	]

	problems = []
	covered = set()
	language = None
	for line in Path(__file__).with_name("check_fixtures.txt").read_text().splitlines():
		if not line or line.startswith("#"):
			continue
		if line in SECTIONS:
			language = SECTIONS[line]
			continue
		expected, text = line.split(" ", 1)
		rejected_by = [h["id"] for h in hooks if h["language"] == language and rejects(h, text, config)]
		if rejected_by != ([] if expected == "ok" else [expected]):
			problems.append(f"{text}: expected {expected}, rejected by {rejected_by or 'nothing'}")
		covered.update(rejected_by)

	problems += [f"{h['id']}: no fixture is rejected by this check" for h in hooks if h["id"] not in covered]
	print("\n".join(problems))
	return 1 if problems else 0


if __name__ == "__main__":
	sys.exit(main())
