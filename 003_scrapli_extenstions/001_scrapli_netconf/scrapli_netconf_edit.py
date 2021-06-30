#!/usr/bin/env python

import os

from rich import print
from scrapli_netconf.driver import NetconfDriver

# Create device dict()
device = {
    "host": "172.29.151.7",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "port": 830,
}

# Instantiate Scrapli NETCONF driver with device dict()
conn = NetconfDriver(**device)

# Open connection
conn.open()

# Define interface config payload
interface_config = """
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet7</name>
            <config>
                <description>Scrapli Netconf Demo</description>
                <name>Ethernet7</name>
                <enabled>true</enabled>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                    <config>
                        <interface-mode>TRUNK</interface-mode>
                        <trunk-vlans>1..110</trunk-vlans>
                    </config>
                </switched-vlan>
            </ethernet>
        </interface>
    </interfaces>
</config>
"""

# Edit config in running datastore with interface config
response = conn.edit_config(config=interface_config, target="running")

# Print result of edit config operation
print(f"edit_config: {response.result}")

# Close connection
conn.close()
