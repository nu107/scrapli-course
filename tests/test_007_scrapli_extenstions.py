import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_scrapli_netconf_capabilities():
    p = importlib.import_module(
        "003_scrapli_extenstions.001_scrapli_netconf.scrapli_netconf_capabilities"
    )

    assert len(p.conn.server_capabilities) > 0


def test_scrapli_netconf_connection():
    p = importlib.import_module(
        "003_scrapli_extenstions.001_scrapli_netconf.scrapli_netconf_connection"
    )

    assert p is not None


def test_scrapli_netconf_edit():
    p = importlib.import_module(
        "003_scrapli_extenstions.001_scrapli_netconf.scrapli_netconf_edit"
    )

    assert (
        '<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"'
        in p.response.result
    )


def test_scrapli_netconf_get():
    p = importlib.import_module(
        "003_scrapli_extenstions.001_scrapli_netconf.scrapli_netconf_get"
    )

    assert (
        '<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"'
        in p.response.result
    )


def test_scrapli_cfg_getters():
    p = importlib.import_module(
        "003_scrapli_extenstions.002_scrapli_cfg.scrapli_cfg_getters"
    )

    assert os.path.isfile(p.BACKUP_FILENAME)
    assert os.path.getsize(p.BACKUP_FILENAME) > 0


def test_scrapli_cfg_commit_abort():
    p = importlib.import_module(
        "003_scrapli_extenstions.002_scrapli_cfg.scrapli_cfg_commit_abort"
    )

    assert p.commit_result is not None


def test_scrapli_cfg_connection():
    p = importlib.import_module(
        "003_scrapli_extenstions.002_scrapli_cfg.scrapli_cfg_connection"
    )
    expected = [
        "abort_config",
        "candidate_config",
        "cleanup",
        "clear_config_sessions",
        "commit_config",
        "config_session_name",
        "config_sources",
        "conn",
        "dedicated_connection",
        "diff_config",
        "get_config",
        "get_version",
        "ignore_version",
        "load_config",
        "logger",
        "on_prepare",
        "prepare",
        "render_substituted_config",
    ]
    assert all(elem in dir(p.cfg_conn) for elem in expected)


def test_scrapli_cfg_load_diff():
    p = importlib.import_module(
        "003_scrapli_extenstions.002_scrapli_cfg.scrapli_cfg_load_diff"
    )

    assert True


def test_scrapli_nornir_functions():
    p = importlib.import_module(
        "003_scrapli_extenstions.003_scrapli_nornir.scrapli_nornir_functions"
    )

    assert p.results is not None


def test_scrapli_nornir_response():
    p = importlib.import_module(
        "003_scrapli_extenstions.003_scrapli_nornir.scrapli_nornir_response"
    )

    assert p.results["spine1-nxos"].scrapli_response.textfsm_parse_output() is not None
    assert p.results["spine1-nxos"].scrapli_response.failed == False
    assert p.results["spine1-nxos"].scrapli_response.elapsed_time > 0


def test_scrapli_nornir_tasks():
    p = importlib.import_module(
        "003_scrapli_extenstions.003_scrapli_nornir.scrapli_nornir_tasks"
    )

    assert p.results is not None
