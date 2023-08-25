"""
module: asyncio

a demo of async function
"""

import asyncio

async def main():
    print("main func")


print("start")
asyncio.run(main())
print("end")
