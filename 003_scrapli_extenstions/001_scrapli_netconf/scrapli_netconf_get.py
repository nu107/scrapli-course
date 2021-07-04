#!/usr/bin/env python

import os

from rich import print
from scrapli_netconf.driver import NetconfDriver

# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "port": 9831,
}


# Instantiate Scrapli NETCONF driver with device dict()
conn = NetconfDriver(**device)

# Open connection
conn.open()

# Get config from running datastore
response = conn.get_config(source="running")

# Print the retrieved config
print(f"get_config: {response.result}")

# Close connection
conn.close()
