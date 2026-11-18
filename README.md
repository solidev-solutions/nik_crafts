### NichtImKopf Crafts Community

Business software for small craft businesses, built on ERPNext

### Installation

This app needs [ERPNext](https://github.com/frappe/erpnext) version 16. You can install it using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app erpnext --branch version-16
bench get-app https://github.com/solidev-solutions/nik_crafts --branch version-16
bench install-app nik_crafts
```

### Contributing

Pull requests target the `develop` branch. Run `pre-commit install` once, then the checks run on every commit.

### License

[AGPL-3.0-or-later](license.txt). Copyright (c) 2026, Solidev - Thomas Liska and contributors.
