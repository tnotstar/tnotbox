/* bigquery.go */

package main

import (
    "fmt"
    "log"
    "golang.org/x/oauth2"
    "golang.org/x/oauth2/google"
)

func main() {

    config := &oauth2.Config{
        ClientID: "245270318409-k4e8t7u4iosdhjar7m95hdjt8suv3o31.apps.googleusercontent.com",
        ClientSecret: "F4LGq54XZTHdypQ9v7m2hNBR",
        Scopes: []string{
            "https://www.googleapis.com/auth/bigquery",
        },
        Endpoint: google.Endpoint,
    }

    url := config.AuthCodeURL("state")
    fmt.Printf("Visit the URL for the auth dialog: %v\n", url)
    token, err := config.Exchange(oauth2.NoContext, "authorization-code")
    if err != nil {
        log.Fatal(err)
    }
    client := config.Client(oauth2.NoContext, token)
    client.Get("...")


//    svc, err := bq.New(oauthHttpClient)
}

/* EOF */
