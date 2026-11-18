"""Test the repository's own checks on file names against the examples in check_fixtures.txt.

Each fixture line names the check that must reject a path, or "ok" when none may.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
FIXTURES = Path(__file__).with_name("check_fixtures.txt").read_text().splitlines()
# Settings that change which files a check sees and that this test does not model.
NOT_MODELLED = ("types", "types_or", "exclude_types")


def rejects(hook: dict, path: str) -> bool:
	"""A `fail` check rejects every file it runs on: `files` matches it and no `exclude` does."""
	return bool(
		re.search(hook.get("files", ""), path)
		and not re.search(hook.get("exclude", "^$"), path)
		and not re.search(CONFIG.get("exclude", "^$"), path)
	)


def main() -> int:
	hooks = [
		hook
		for repo in CONFIG["repos"]
		if repo["repo"] == "local"
		for hook in repo["hooks"]
		if hook["language"] == "fail"
	]
	problems = [
		f"{hook['id']}: this test does not model {key}"
		for hook in hooks
		for key in NOT_MODELLED
		if key in hook
	]

	without_fixture = {hook["id"] for hook in hooks}
	for number, line in enumerate(FIXTURES, start=1):
		if not line or line.startswith("#"):
			continue
		expected, _, path = line.partition(" ")
		if not path:
			problems.append(f"line {number}: no path: {line}")
			continue
		rejected_by = [hook["id"] for hook in hooks if rejects(hook, path)]
		if rejected_by != ([] if expected == "ok" else [expected]):
			problems.append(
				f"line {number}: {path}: expected {expected}, rejected by {rejected_by or 'nothing'}"
			)
		without_fixture -= set(rejected_by)

	problems += [f"{check}: no fixture is rejected by this check" for check in sorted(without_fixture)]
	if problems:
		print("\n".join(problems))
	return 1 if problems else 0


if __name__ == "__main__":
	sys.exit(main())
