#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli
from scrapli.logging import enable_basic_logging

load_dotenv()

# Enable logging. Create a log file in the current directory.
enable_basic_logging(file=True, level="debug")

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
    # Send command to device
    response = conn.send_command("show run")

# Print command response
print(response.result)
