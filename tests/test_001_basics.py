import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_scrapli_basic():
    p = importlib.import_module("002_scrapli_core.001_basics.scrapli_basic")

    assert "!Command: show running-config" in p.response.result


def test_scrapli_context_manager():
    p = importlib.import_module("002_scrapli_core.001_basics.scrapli_context_manager")

    assert "!Command: show running-config" in p.response.result


def test_scrapli_logging():
    p = importlib.import_module("002_scrapli_core.001_basics.scrapli_logging")

    assert "!Command: show running-config" in p.response.result
    assert os.path.isfile("scrapli.log") == True
    assert os.path.getsize("scrapli.log") > 0
