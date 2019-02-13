#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

async def send_echo_request(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 9888, loop=loop)
    print("Send: %r" % message)
    writer.write(message.encode())

    buffer = await reader.read(128)
    print("Received %r" % buffer.decode())

    writer.close()
    print("Close socket!")

if __name__ == "__main__":
    message = "Hello, world!"
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_echo_request(message, loop))
    loop.close()

# EOF