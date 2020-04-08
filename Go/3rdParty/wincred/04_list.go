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

// EOF