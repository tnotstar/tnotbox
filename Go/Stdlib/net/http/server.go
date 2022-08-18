package main

import (
    "net/http"
    "fmt"
    "log"
)

func main() {
    http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, world!")
    })

    log.Print("Starting server at port :5555...")
    http.ListenAndServe(":5555", nil)
}
