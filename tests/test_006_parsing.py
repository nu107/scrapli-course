import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_genie_scrapli_genie_library():
    p = importlib.import_module(
        "002_scrapli_core.006_parsing.genie.scrapli_genie_library"
    )
    expected = {
        "interface": {
            "Lo0": {
                "ip_address": "11.11.11.11",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/1": {
                "ip_address": "10.1.1.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/2": {
                "ip_address": "10.1.2.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/3": {
                "ip_address": "10.1.3.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/4": {
                "ip_address": "10.1.4.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/5": {
                "ip_address": "10.1.5.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
            "Eth1/6": {
                "ip_address": "10.1.6.1",
                "interface_status": "protocol-up/link-up/admin-up",
            },
        }
    }
    assert p.genie_parsed_response == expected


def test_parsing_textfsm_scrapli_textfsm_custom():
    p = importlib.import_module(
        "002_scrapli_core.006_parsing.textfsm.scrapli_textfsm_custom"
    )

    assert sorted(list(p.textfsm_parsed_response[0].keys())) == sorted(
        ["load_average", "time", "uptime", "users"]
    )


def test_parsing_textfsm_scrapli_textfsm_library():
    p = importlib.import_module(
        "002_scrapli_core.006_parsing.textfsm.scrapli_textfsm_library"
    )

    assert type(p.textfsm_parsed_response[0]) is dict


def test_parsing_ttp_scrapli_ttp_custom():
    p = importlib.import_module("002_scrapli_core.006_parsing.ttp.scrapli_ttp_custom")

    assert (
        p.ttp_parsed_response is not None and type(p.ttp_parsed_response[0][0]) is dict
    )


def test_parsing_ttp_generic():
    p = importlib.import_module("002_scrapli_core.006_parsing.ttp.ttp_generic")

    assert '"vlan_id": "1",' in p.results
