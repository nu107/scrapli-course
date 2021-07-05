#!/usr/bin/env python

import os

from rich import print
from scrapli import Scrapli

# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "port": 9007,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "arista_eos",
}

# Helper function 
def get_absolute_path(filename):
    # Get absolute path to command file
    absolute_path = os.path.dirname(os.path.realpath(__file__))
    return f"{absolute_path}/{filename}"

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send command to device
    response = conn.send_command("show interfaces")

    # Get TTP parsed response
    ttp_template = get_absolute_path("eos_show_interfaces.ttp")
    ttp_parsed_response = response.ttp_parse_output(template=ttp_template)

# Print parsed response
print(ttp_parsed_response)
