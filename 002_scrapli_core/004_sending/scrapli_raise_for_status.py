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
    # Send commands to device
    commands = ["show version", "show foobar"]
    multiresponse = conn.send_commands(commands)

    # Print Response attributes if they have not failed
    for response in multiresponse:
        if not response.failed:
            print(
                f"{response.channel_input} = elapsed_time {response.elapsed_time}"
            )

# Raise an exeception if any command has failed
multiresponse.raise_for_status()
