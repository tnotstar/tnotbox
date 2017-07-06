#!/bin/sh
exec scala "$0" "$@"
!#

object HelloScript {
    def main(args: Array[String]): Unit = {
        println("Hello, world!")
    }
}
