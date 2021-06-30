#!/usr/bin/env python

import os

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Init Nornir with Nornir config file
config_file = (
    "003_scrapli_plugins_extenstions/003_scrapli_nornir/nornir/config.yaml"
)
nr = InitNornir(config_file=config_file)

# Set inventory credentials from environment variables
nr.inventory.defaults.username = os.getenv("LAB_USERNAME")
nr.inventory.defaults.password = os.getenv("LAB_PASSWORD")

# Filter only nxos based devices
nr = nr.filter(platform="nxos")

# Run the Scrapli send command task against the filter devices
results = nr.run(task=send_command, command="show ip ospf neighbor")

# Print the results from all the run tasks
print_result(results)
