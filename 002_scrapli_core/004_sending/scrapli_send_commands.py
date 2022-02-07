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
    # Send commands to device
    commands = ["show version", "show ip interface brief"]
    multiresponse = conn.send_commands(commands)

    # Print MultiResponse attributes
    print(multiresponse.result)
    print(multiresponse.failed)

    # Print Response attributes
    print("---")
    for response in multiresponse:
        print(f"{response.channel_input} = elapsed_time {response.elapsed_time}")
