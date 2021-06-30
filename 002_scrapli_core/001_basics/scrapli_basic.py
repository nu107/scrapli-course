#!/usr/bin/env python

import os

from rich import print
from scrapli import Scrapli

# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "port": 9007,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "arista_eos",
}

# Instantiate Scrapli driver with device dict()
conn = Scrapli(**device)

# Open connection to device
conn.open()

# View available Driver methods
print(dir(conn))

# Send command to device
response = conn.send_command("show run")

# Print command response
print(response.result)

# Close connection
conn.close()
