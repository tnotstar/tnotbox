// Copyright 2020-22, Antonio Alvarado Hernández

package main

import (
    "os";
    "fmt";
    "net/http";
    "io/ioutil";
)

func main() {
    res, err := http.Get("http://www.yahoo.es")
    if err != nil {
        fmt.Println("Oops: something is wrong...")
        os.Exit(1)
    }
    defer res.Body.Close()

    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println("Oops: can't read response's body")
        os.Exit(2)
    }

    fmt.Println(string(body[:128]))
}
