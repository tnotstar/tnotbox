package main

import (
    "fmt"

    "github.com/danieljoos/wincred"
)

func main() {
    fmt.Println("Beginning...")
    creds, err := wincred.List()
    if err != nil {
        fmt.Println(err)
        return
    }
    for i := range(creds) {
        fmt.Println(">", creds[i].TargetName)
    }
    fmt.Println("Finished!")
}
