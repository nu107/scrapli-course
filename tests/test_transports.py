import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_transports_scrapli_ssh2_transport():
    p = importlib.import_module(
        "002_scrapli_core.002_transports.scrapli_ssh2_transport"
    )

    assert "!Command: show running-config" in p.response.result
