#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli

load_dotenv()

# Create device dict()
device = {
    "host": "172.29.151.1",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}

# Instantiate Scrapli driver with device dict()
conn = Scrapli(**device)

# Open connection to device
conn.open()

# View available Driver methods
# print(dir(conn))

# Send command to device
response = conn.send_command("show run")

# Print command response
print(response.result)

# Close connection
conn.close()
