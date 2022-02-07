#!/usr/bin/env python

import os

from dotenv import load_dotenv
from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

from helpers import read_file, write_file

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

    # Get device config for demo purposes
    get_config_result = cfg_conn.get_config(source="running").result
    write_file(filename=BACKUP_FILENAME, data=get_config_result)

    # Configure device for demo purposes
    commands = ["interface loopback200", "description # Scrapli Cfg Demo"]
    multiresponse = conn.send_configs(commands)

    # Load configuration as candidate
    load_result = cfg_conn.load_config(
        config=read_file(filename=BACKUP_FILENAME), replace=True
    )

    # Print differences
    # Other diff outputs - device_diff, unified_diff, additions, subtractions
    diff_result = cfg_conn.diff_config()
    print(diff_result.side_by_side_diff)
