#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

from helpers import write_file

load_dotenv()

BACKUP_FILENAME = "running-config.txt"

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

    # Get device config
    get_config_result = cfg_conn.get_config(source="running").result
    write_file(filename=BACKUP_FILENAME, data=get_config_result)

    # Get device version
    get_version_result = cfg_conn.get_version().result

    # Print summary
    print(f"Device version = {get_version_result}, Config saved = {BACKUP_FILENAME}")
