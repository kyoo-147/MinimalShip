# Installation boundary

The installer may copy public product-development guidance and promoted skill metadata. It must not copy repository governance, local analysis, credentials, Git data, project run records, or machine-specific configuration. It installs the root bundle and promoted skills as separate Pi-discoverable directories.

It must not download packages, execute project hooks, create a cloud resource, authenticate a provider, or modify any destination when an existing root or promoted skill is present without `--force`.
