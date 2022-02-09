#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uvicorn


async def app(scope, receive, send):
    assert scope["type"] == "http"

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            [b"Content-Type", b"text/plain"],
        ],
    })

    await send({
        "type": "http.response.body",
        "body": b"Hello, world!",
    })


if __name__ == "__main__":
    uvicorn.run("hello:app", host="127.0.0.1", port=8001, log_level="info")

# EOF
