#!/bin/sh
exec scala "$0" "$@"
!#

object HelloScript extends App {

    println("Hello, world!")
}

HelloScript.main(args)

