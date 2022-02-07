import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_scrapli_raise_for_status():
    import scrapli

    try:
        p = importlib.import_module(
            "002_scrapli_core.004_sending.scrapli_raise_for_status"
        )
        assert False
    except scrapli.exceptions.ScrapliException:
        assert True


def test_scrapli_send_command():
    p = importlib.import_module("002_scrapli_core.004_sending.scrapli_send_command")

    assert "Cisco Nexus Operating System (NX-OS) Software" in p.response.result
    assert p.response.failed == False
    assert p.response.elapsed_time > 0


def test_scrapli_send_commands_from_file():
    p = importlib.import_module(
        "002_scrapli_core.004_sending.scrapli_send_commands_from_file"
    )

    assert "Cisco Nexus Operating System (NX-OS) Software" in p.multiresponse.result
    assert p.multiresponse.failed == False
    for response in p.multiresponse:
        assert response.channel_input is not None
        assert response.elapsed_time > 0


def test_scrapli_send_commands():
    p = importlib.import_module("002_scrapli_core.004_sending.scrapli_send_commands")

    assert "Cisco Nexus Operating System (NX-OS) Software" in p.multiresponse.result
    assert p.multiresponse.failed == False
    for response in p.multiresponse:
        assert response.channel_input is not None
        assert response.elapsed_time > 0


def test_scrapli_send_interactive():
    p = importlib.import_module("002_scrapli_core.004_sending.scrapli_send_interactive")

    assert True
