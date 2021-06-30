#!/usr/bin/env python

import os

from rich import print
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
    # Send config to device
    send_configs_file = (
        f"{os.path.dirname(os.path.realpath(__file__))}/config_commands.txt"
    )
    multiresponse = conn.send_configs_from_file(send_configs_file)

# Print MultiResponse attributes
print(multiresponse.result)
print(multiresponse.failed)
