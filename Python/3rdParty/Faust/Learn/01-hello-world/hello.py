# -*- coding: utf-8 -*-

import faust


app = faust.App(
    id="hello",
    value_serializer="raw"
)

greetings_topic = app.topic("greetings")


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)


if __name__ == "__main__":
    print("Hello, world!")

