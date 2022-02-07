#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

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
    # Instantiate Scrapli Cfg
    cfg_conn = ScrapliCfg(conn=conn)

    # Prepare Scrapli connection, call prepare_on() etc
    cfg_conn.prepare()

    # Get ScrapliCfg properties and methods
    print(dir(cfg_conn))
