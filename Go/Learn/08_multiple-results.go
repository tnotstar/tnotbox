/* 08_multiple-results.go */

package main

import "fmt"

func swap(x, y string) (string, string) {
    return y, x
}

func main() {
    a, b := swap("hello", "world")
    fmt.Printf("a = \"%s\" and b = \"%s\"\n", a, b)
}

/* EOF */
