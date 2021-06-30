#!/usr/bin/env python

import os

from rich import print
from scrapli import Scrapli

IP_ROUTE = "9.9.9.9/32"

# Function to perform just before connection is closed
def save_on_close(conn):
    """Perform wr mem before connection close"""
    conn.channel.send_input("wr mem")
    print("Config saved to startup")


# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "port": 9007,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "arista_eos",
    "on_close": save_on_close,
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send config command to device
    response = conn.send_config(f"ip route {IP_ROUTE} null0")

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send config command to device
    response = conn.send_command(f"show startup-config | grep {IP_ROUTE}")
    conn.send_config(f"no ip route {IP_ROUTE} null0")

# Print the contents of the startup config change
print(f"startup-config: {response.result}")
