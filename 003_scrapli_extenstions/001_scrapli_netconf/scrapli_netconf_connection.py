#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli_netconf.driver import NetconfDriver

load_dotenv()

# Create device dict()
device = {
    "host": "172.29.151.7",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
}

# Instantiate Scrapli NETCONF driver with device dict()
conn = NetconfDriver(**device)

# Open connection
conn.open()

# Close connection
conn.close()
