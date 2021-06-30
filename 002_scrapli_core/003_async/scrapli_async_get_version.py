#!/usr/bin/env python

import asyncio

from inventory_external import DEVICES
from rich import print
from scrapli_cfg import AsyncScrapliCfg


# declare function as a coroutine via async keyword
async def gather_version(device):
    # Create async connection. Set as awaitable
    async_conn = device.pop("driver")(**device)

    # Open async connection - Set as awaitable
    await async_conn.open()

    # Create Scrapli Cfg async connection
    async_cfg_conn = AsyncScrapliCfg(conn=async_conn, ignore_version=True)

    # Prepare Scrapli Cfg async connection - Set as awaitable
    await async_cfg_conn.prepare()

    # Get device prompt and version - Set as awaitables
    prompt_result = await async_conn.get_prompt()
    version_result = await async_cfg_conn.get_version()

    # Close connection - Set as awaitable
    await async_conn.close()

    # Return results
    return prompt_result, version_result


# declare function as a coroutine via async keyword
async def main():
    # Create list of coroutines
    coroutines = [gather_version(device) for device in DEVICES]

    # Run coroutines concurrently - Set as awaitable
    results = await asyncio.gather(*coroutines)

    # Print results
    for result in results:
        print(f"{result[0],} ---> {result[1].result}")


if __name__ == "__main__":
    # Create event loop and run main()
    asyncio.get_event_loop().run_until_complete(main())
