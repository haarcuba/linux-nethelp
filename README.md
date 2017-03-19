# LINUX NetHelp

NetHelp is a package of helpers - I started it because I needed to find out which of my network interfaces belongs to which IP subnet. Couldn't find anything that I liked, so I made this small library.

Currently, it only supports this functionality - but as the need arrises, features may add up.

# Installation

    $ pip install linux-nethelp

Now you can:

```python
from linux_nethelp.scan_interfaces import ScanInterfaces
import pprint

interfaces = list( ScanInterfaces() )
pprint.pprint( interfaces )
```

sample output:
```python
[{'ip': '127.0.0.1', 'ip/mask': '127.0.0.1/8', 'mask': '8', 'name': 'lo'},
 {'ip': '172.17.0.1',
  'ip/mask': '172.17.0.1/16',
  'mask': '16',
  'name': 'docker0'},
 {'ip': '192.168.122.1',
  'ip/mask': '192.168.122.1/24',
  'mask': '24',
  'name': 'virbr0'},
 {'ip': '10.20.20.1',
  'ip/mask': '10.20.20.1/24',
  'mask': '24',
  'name': 'vboxnet0'},
 {'ip': '10.30.30.210',
  'ip/mask': '10.30.30.210/24',
  'mask': '24',
  'name': 'wlx00116bd8626e'}]
```
