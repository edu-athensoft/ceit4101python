"""

"""

import asyncio
import time


async def long_running_function():
    print("running long_running_function()")
    # sleep for 3 secs
    for i in range(3,-1, -1):
        print("\r"+str(i), flush=True, end="")
        time.sleep(1)


    print("\njob finished.")
    # pass


async def main():
    await long_running_function()

    # wait till long_running_function() finished
    print('Done!')


# run
asyncio.run(main())
