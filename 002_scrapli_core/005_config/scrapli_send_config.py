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

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send config command to device
    response = conn.send_config("ip route 1.2.3.4/32 null0")

# Print response summary
print(response)
