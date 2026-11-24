# Agent instructions

NichtImKopf Crafts Community (`nik_crafts`) is business software for craft businesses with 3 to 30 people. It is a Frappe app built on ERPNext 16, without HRMS. Frappe and ERPNext come first: the app adds its own code only where the native way cannot do the job.

## Before you write code

- Look for what already exists. Check how Frappe and ERPNext solve the problem: a DocType, a field, a setting, a hook, a report. Grep their source in the bench before you design anything.
- Read the official documentation of the mechanism you are about to use, and use it the way it describes. Do not build your own where a documented way exists.
- Learn how a feature is built from the features already in this repository, and build the next one the same way.

## Making the change

- Make the smallest correct change. Do not reformat, rename or move code you did not need to touch.
- Write code that needs no comment. Add one only where the code cannot say it itself: a reason that is not obvious, a limit, a workaround. A comment states the condition that holds today, never the way there.
- What a tool can check becomes a check in `.pre-commit-config.yaml`, not a sentence in a file.
- Everything in this repository is English. German reaches the interface through Frappe's translations.

## Architecture

- DocType files come from saving the DocType in developer mode, never from writing them by hand.
- Code moves to `nc_core/` or `engine/` once a second feature uses it or a planned feature will. The pull request names that feature.
- `contract.py` hands out plain values and models from `domain/`, never Frappe documents.
- Reading, saving and deleting a record never get an endpoint of their own.
- A feature names neither the DocType nor the module path of another feature as a string. It goes through that feature's `contract.py`.

## Commands

- Checks: `pre-commit run --files <changed files>`.
- After changing a `uses:` line in a workflow: `gh actions-lock`, from the gh extension `github/gh-actions-lock`.
- Tests: `bench --site <site> run-tests --app nik_crafts`, or `--module <dotted.path>` for one module.
- Run tests on a throwaway site. Site names, ports and credentials belong to your machine and never to this repository.

## Pull requests

- Target `develop`. The title becomes the commit, so write it as one: `fix(quotation): keep the company on copy`.
- The description says in a few plain sentences what the change is about, and in one line what was checked or that nothing was. No lists, tables or links.
- Commits and pull requests carry no AI attribution line.

## Never

- Never report something as tested, reproduced or checked that did not run.
- Never bypass permissions to make something work. Where the design calls for a bypass, the checks say where it stands and how the line above it names the reason.
- Never write to ERPNext's tables directly. Change its data through the document: `save`, `submit`, `cancel`.
