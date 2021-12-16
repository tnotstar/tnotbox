# -*- coding: utf-8 -*-


def hello(who: str = None) -> None:
    if who:
        print(f"Hello, {who}!")
    else:
        print("Hello, world!")


# EOF
