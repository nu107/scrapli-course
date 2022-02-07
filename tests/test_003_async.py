import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_async_get_version():
    sys.path.append(r"002_scrapli_core/003_async")

    p = importlib.import_module("002_scrapli_core.003_async.scrapli_async_get_version")
    p.asyncio.get_event_loop().run_until_complete(p.main())

    assert True
