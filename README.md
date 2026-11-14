### NichtImKopf Crafts Community

Business software for small craft businesses, built on ERPNext

### Installation

This app needs [ERPNext](https://github.com/frappe/erpnext) version 16. You can install it using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app erpnext --branch version-16
bench get-app https://github.com/solidev-solutions/nik_crafts --branch develop
bench install-app nik_crafts
```

There is no release yet. Releases will be published on the `version-16` branch.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/nik_crafts
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier

Pull requests target the `develop` branch. Their title follows [Conventional Commits](https://www.conventionalcommits.org/), for example `fix(quotation): keep the company on copy`.

### License

[AGPL-3.0-or-later](license.txt). Copyright (c) 2026, Solidev - Thomas Liska and contributors.
