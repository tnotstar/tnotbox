//usr/bin/env go run "$0" "$@"; exit "$?"
// -*- coding: utf-8 -*-
//
// Copyright (c) 2019-2020 Antonio Alvarado Hernández
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
    "os"
    "fmt"
    "github.com/pkg/errors"
)

func raiseAnError() error {
    _, err := os.Open("this file won't find")
    if err != nil {
        return errors.Wrap(err, "Oops this file hasn't found")
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