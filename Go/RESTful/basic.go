/* basic.go */

package main

import (
    "fmt"
    "html"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(writer http.ResponseWriter, req *http.Request) {
    fmt.Fprintf(writer, "Hello, %q! (from Basic)\n", html.EscapeString(req.URL.Path))
}

/* EOF */
