/* fetch.go */

package main

import "fmt"
import "time"
import "net/http"

func main() {
	start := time.Now()
	http.Get("http://www.yahoo.com")
	fmt.Println(time.Since(start))
}

/* EOF */