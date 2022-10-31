package main

import (
	"encoding/json"
)

type Struct struct {
    Value float64 `json:"pi"`
}

func main() {
	t := Struct{Value: 3.141516}

	b, err := json.Marshal(t)
	if err != nil {
		panic(err)
	}

	var newT Struct
	_ = json.Unmarshal(b, &newT)
	if t != newT {
		panic("Oops: something is wrong!")
	}
}
