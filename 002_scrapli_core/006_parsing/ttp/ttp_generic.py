#!/usr/bin/env python

from rich import print
from ttp import ttp

vlan_data = """
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active
100   VLAN100                          active
200   VLAN200                          active
300   VLAN300                          active
"""

ttp_template = """
{{ vlan_id }}   {{ vlan_name }}                          active
"""

parser = ttp(data=vlan_data, template=ttp_template)
parser.parse()

results = parser.result(format="json")[0]

if __name__ == "__main__":
    print(results)
