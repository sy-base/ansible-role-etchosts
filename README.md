etchosts
=========

Simple role to manage the contents of hosts file on *nix systems.

Requirements
------------

This role has no additional requirements.

Role Variables
--------------
```yaml
etchosts_file - String Value containing the absolute path to your system's hosts file. This defaults to "/etc/hosts".
etchosts_local_entries - Boolean (True/False). Should entries for 127.0.0.1 (IPv4 localhost)  and ::1 (IPv6 localhost) be include in the hosts file by default
etchosts_entries - Dict Value containing entries that should reside in your system's hosts file. Example:

etchosts_entries:
  - host: hostname.local
    address: 192.168.0.1
    secondary_hostnames:
      - hostname
      - hostname-alias
```

Dependencies
------------

No Dependencies.

Example Playbook
----------------
```yaml
---
- hosts: servers
  tasks:
    - include_role:
        name: sy-base.etchosts
      vars:
        etchosts_file: /etc/hosts
        etchosts_local_entries: True
        etchosts_entries:
          - host: myserver.local
            address: 192.168.0.1
            secondary_hostnames:
              - myserver
```

Example Output
--------------
```
127.0.0.1       localhost localhost.localdomain localhost4 localhost4.localdomain4
::1             localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.0.1	myserver.local myserver
```

License
-------

BSD

Author Information
------------------

sybase - https://github.com/sy-base
