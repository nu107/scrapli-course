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
    "port": 9837,
}

# Instantiate Scrapli NETCONF driver with device dict()
conn = NetconfDriver(**device)

# Open connection
conn.open()

# Print devices capabilities
print(conn.server_capabilities)

# Close connection
conn.close()
