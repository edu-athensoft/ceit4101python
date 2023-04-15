"""
coroutine
async
await
"""

import asyncio
import time


async def long_running_function(secs):
    print(f"running long_running_function({secs}) - {secs} seconds needed.")
    # sleep for 3 secs
    for i in range(secs,-1, -1):
        print("\r"+str(i), flush=True, end="")
        time.sleep(1)


    print("\njob finished.")
    # pass


async def main():
    await long_running_function(5)
    await long_running_function(3)

    # wait till long_running_function() finished
    print('\n\nDone!')


# run
asyncio.run(main())
