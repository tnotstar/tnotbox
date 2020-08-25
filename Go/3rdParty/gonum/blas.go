// -*- coding: utf-8 -*-
//
// Copyright (c) 2016-2020 Antonio Alvarado Hernández
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

import "fmt"
import "github.com/gonum/blas/blas64"

func main() {

    v := blas64.Vector{Inc: 1, Data: []float64{1, 1, 1}}
    fmt.Println("v has length:", blas64.Nrm2(len(v.Data), v))
}

// EOF