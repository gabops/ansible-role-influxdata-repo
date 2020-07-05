gabops.influxdata_repo
======================

![Molecule CI](https://github.com/gabops/ansible-role-influxdata-repo/workflows/Molecule%20CI/badge.svg?branch=master)

Installs and configures Influxdata official repository.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| influxdata_repo_state | present | Controls whether or not influxdata repo is installed. Possible values are `present` or `absent`. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gabops.influxdata_repo
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
