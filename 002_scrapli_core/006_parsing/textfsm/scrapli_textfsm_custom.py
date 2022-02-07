#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli
from scrapli.helper import textfsm_parse

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
    response = conn.send_command("show uptime")

    # TextFSM parse response
    textfsm_template = (
        f"{os.path.dirname(os.path.realpath(__file__))}/eos_show_uptime.textfsm"
    )
    textfsm_parsed_response = textfsm_parse(
        textfsm_template,
        response.result,
    )

# Print parsed response
print(textfsm_parsed_response)
