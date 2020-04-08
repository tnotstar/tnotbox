package main

import (
    "fmt"

    "github.com/danieljoos/wincred"
)

func main() {
    fmt.Println("Beginning...")
    cred := wincred.NewGenericCredential("Test-Application")
    cred.CredentialBlob = []byte("This is my secret password!!")
    err := cred.Write()
    if err != nil {
        fmt.Println(err)
    }
    fmt.Println("Finished!")
}
