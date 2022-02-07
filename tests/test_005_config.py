import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_scrapli_save_on_close():
    p = importlib.import_module("002_scrapli_core.005_config.scrapli_save_on_close")

    assert "9.9.9.9/32" in p.response.result


def test_scrapli_send_config():
    p = importlib.import_module("002_scrapli_core.005_config.scrapli_send_config")

    assert p.response.failed == False


def test_scrapli_send_configs_from_file():
    p = importlib.import_module(
        "002_scrapli_core.005_config.scrapli_send_configs_from_file"
    )

    assert (
        p.multiresponse.result
        == "vlan 101\n  name VLAN101\nvlan 102\n  name VLAN102\nvlan 103\n  name VLAN103\n"
    )
    assert p.multiresponse.failed == False


def test_scrapli_send_configs():
    p = importlib.import_module("002_scrapli_core.005_config.scrapli_send_configs")

    assert (
        p.multiresponse.result == "interface loopback1000\ndescription # Scrapli Demo\n"
    )
    assert p.multiresponse.failed == False
    for response in p.multiresponse:
        assert response.channel_input is not None
        assert response.elapsed_time > 0
