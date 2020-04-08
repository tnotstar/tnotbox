// -*- coding: utf-8 -*-
//
// Copyright (c) 2020 Antonio Alvarado Hernández - All rights reserved
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//

package main

import (
    "os";
    "fmt";
    "io/ioutil";
    "net/http";
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
