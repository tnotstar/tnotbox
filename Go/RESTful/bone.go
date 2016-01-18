/* bone.go */

package main

import (
    "fmt"
    "html"
    "log"
    "net/http"
    "github.com/go-zoo/bone"
)

func main() {
    mux := bone.New()
    mux.Handle("/", http.HandlerFunc(handler))
    log.Fatal(http.ListenAndServe(":8080", mux))
}

func handler(writer http.ResponseWriter, req *http.Request) {
    fmt.Fprintf(writer, "Hello, %q! (from Bone)\n", html.EscapeString(req.URL.Path))
}

/* EOF */
