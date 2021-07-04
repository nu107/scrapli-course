#!/usr/bin/env python

import os

from nornir import InitNornir
from nornir_scrapli.functions import print_structured_result
from nornir_scrapli.tasks import send_command

# Init Nornir with Nornir config file
config_file = "003_scrapli_extenstions/003_scrapli_nornir/nornir/config.yaml"
nr = InitNornir(config_file=config_file)

# Set inventory credentials from environment variables
nr.inventory.defaults.username = os.getenv("LAB_USERNAME")
nr.inventory.defaults.password = os.getenv("LAB_PASSWORD")

# Filter only nxos based devices
nr = nr.filter(platform="nxos")

# Run the Scrapli send command task against the filter devices
results = nr.run(task=send_command, command="show ip ospf neighbor")

# Print the results from all the run tasks
print_structured_result(results, parser="textfsm", fail_to_string=True)
