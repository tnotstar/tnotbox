package main

import (
    "fmt"

    "github.com/danieljoos/wincred"
)

func main() {
    fmt.Println("Beginning...")
    cred, err := wincred.GetGenericCredential("Test-Application")
    if err != nil {
        fmt.Println(err)
    }

    fmt.Println(">", string(cred.CredentialBlob))
    fmt.Println("Finished!")
}
