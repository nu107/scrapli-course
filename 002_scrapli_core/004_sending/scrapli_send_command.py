#!/usr/bin/env python

import os

from rich import inspect, print
from scrapli import Scrapli

# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "port": 9001,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send command to device
    response = conn.send_command("show version")

    # Inspect response object
    inspect(response)

    # Print common response attributes
    print(response.result)
    print(response.failed)
    print(response.elapsed_time)
