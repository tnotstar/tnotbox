#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

async def handle_echo_request(reader, writer):
    """Handle echo requests from connected clients."""

    buffer = await reader.read(128)

    message = buffer.decode()
    client_address = writer.get_extra_info("peername")
    print("Received %r from %r" % (message, client_address))

    print("Send: %r" % message)
    writer.write(buffer)
    await writer.drain()

    print("Close the client socket")
    writer.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo_request, "127.0.0.1", 9888, loop=loop)
    server = loop.run_until_complete(coro)

    print("Serving on {}".format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

# EOF