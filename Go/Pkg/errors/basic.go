//usr/bin/env go run "$0" "$@"; exit "$?"

package main

import (
    "os"
    "fmt"
    "github.com/pkg/errors"
)

func raiseAnError() error {
    _, err := os.Open("this file won't find")
    if err != nil {
        return errors.Wrap(err, "Oops: this file hasn't found")
    }
    return nil
}

func main() {
    fmt.Println("Beginning...")
    err := raiseAnError()
    fmt.Println(">", err)
    fmt.Println("Finished!")
}

// EOF