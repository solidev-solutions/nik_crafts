### NichtImKopf Crafts Community

Business software for small craft businesses, built on ERPNext

### Installation

This app needs [ERPNext](https://github.com/frappe/erpnext). Each stable branch of the app runs on one major version of Frappe and ERPNext:

| Branch       | Frappe and ERPNext |
| ------------ | ------------------ |
| `version-16` | version 16         |

`pyproject.toml` names the lowest versions the app supports.

You can install it using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app erpnext --branch version-16
bench get-app https://github.com/solidev-solutions/nik_crafts --branch version-16
bench install-app nik_crafts
```

Or build an image with [frappe_docker](https://github.com/frappe/frappe_docker), with this `apps.json`:

```json
[
  {"url": "https://github.com/frappe/erpnext", "branch": "version-16"},
  {"url": "https://github.com/solidev-solutions/nik_crafts", "branch": "version-16"}
]
```

### Contributing

Pull requests target the `develop` branch. Run `pre-commit install` once, then the checks run on every commit.

### License

[AGPL-3.0-or-later](license.txt). Copyright (c) 2026, Solidev - Thomas Liska and contributors.
