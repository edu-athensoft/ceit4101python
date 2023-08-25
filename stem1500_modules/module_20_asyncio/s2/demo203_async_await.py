"""
module: asyncio

a demo of async function
"""

import asyncio


async def main():
    print("main func")
    await work(101)


async def work(workno):
    print("work func - " + str(workno))
    await asyncio.sleep(1)


print("start")
asyncio.run(main())
print("end")
