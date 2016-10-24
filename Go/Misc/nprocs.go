package main

import (
    "runtime"
    "fmt"
)

func main() {
    fmt.Printf("> GOMAXPROCS is %d\n", runtime.GOMAXPROCS(0))
}

