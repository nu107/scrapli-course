#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli

load_dotenv()

# Create device dict()
device = {
    "host": "172.29.151.7",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "arista_eos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send command to device
    response = conn.send_command("show ip interface brief")

    # TextFSM parse response
    textfsm_parsed_response = response.textfsm_parse_output()

# Print parsed response
print(textfsm_parsed_response)
