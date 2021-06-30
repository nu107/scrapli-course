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
    send_commands_file = (
        f"{os.path.dirname(os.path.realpath(__file__))}/send_commands.txt"
    )
    multiresponse = conn.send_commands_from_file(send_commands_file)

    # Print MultiResponse attributes
    print(multiresponse.result)
    print(multiresponse.failed)

    # Print Response attributes
    print("---")
    for response in multiresponse:
        print(
            f"{response.channel_input} = elapsed_time {response.elapsed_time}"
        )
