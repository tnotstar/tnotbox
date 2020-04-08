// -*- coding: utf-8 -*-
//
// Copyright (c) 2020 Antonio Alvarado Hernández
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

	"github.com/c-bata/go-prompt"
)

func completer(d prompt.Document) []prompt.Suggest {
	s := []prompt.Suggest{
		{Text: "users", Description: "store the username and age"},
		{Text: "articles", Description: "store the article text posted by user"},
		{Text: "comments", Description: "store the text commendted to articles"},
	}
	return prompt.FilterHasPrefix(s, d.GetWordBeforeCursor(), true)
}

func main() {
	fmt.Printf("Please select table...")
	t := prompt.Input("> ", completer)
	fmt.Printf("You selected: %v!", t)
}

// EOF