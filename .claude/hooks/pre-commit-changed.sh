#!/usr/bin/env bash
# Stop hook for Claude Code: runs the pre-commit checks on what changed in the working tree.
# Exit 2 hands the output to the agent and keeps its turn open. Any other failure only shows
# a notice to the person at the keyboard.

input=$(cat)
cd "$CLAUDE_PROJECT_DIR" || exit 0

# Nothing changed, so there is nothing to check and no reason to set up the tools the
# configuration names.
[ -z "$(git status --porcelain)" ] && exit 0

if ! command -v pre-commit >/dev/null 2>&1; then
	echo "pre-commit is not installed, the checks did not run" >&2
	exit 1
fi

if ! output=$(pre-commit install-hooks 2>&1); then
	printf 'pre-commit could not set up its tools, the checks did not run\n%s\n' "$output" >&2
	exit 1
fi

output=$(
	{
		git diff --name-only -z HEAD
		git ls-files -z --others --exclude-standard
	} | xargs -0 pre-commit run --files 2>&1
) && exit 0

# The agent already had one turn to fix this. Holding it again would loop on anything it
# cannot fix, such as a file that belongs to someone else.
if grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true' <<<"$input"; then
	printf 'pre-commit still fails after one retry. Files that are not part of the work belong in .git/info/exclude.\n%s\n' "$output" >&2
	exit 1
fi

printf '%s\n\nFix what you created or changed in this turn. Leave files you did not touch as they are and name them in your reply.\n' "$output" >&2
exit 2
