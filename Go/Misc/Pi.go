package main

import (
    "runtime"
)

func f(a float64) float64 {
    return 4.0/(1.0 + a * a)
}

func integrate(start, end int64, ch chan float64) {
    var sum, x, h float64 = 0.0
    var i int64

    for i := start; i < end; i++ {
        x := h * (float64(i) + 0.5)
        sum += f(x)
    }
    ch <- sum * h
}

func main() {
    np := 4
    n := 10
    h := 1.0/float64(n)
    ch := make(chan float64, np)

    runtime.GOMAXPROCS(np)
    for i := 0; i < np; i++ {
        go integrate(int64(i)*n/int64(np), (int64(i)+1)*n/int64(np), ch)
    }
    for i := 0; i < np; i++ {
        pi += <-c
    }

    println("pi = ", pi)
}

