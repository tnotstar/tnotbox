#/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")

if __name__ == "__main__":
    asyncio.run(main())

# EOF