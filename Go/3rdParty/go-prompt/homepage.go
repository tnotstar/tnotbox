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
