package main

import (
	"github.com/gofiber/fiber/v2"
	"log"
)

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, world!")
	})

	err := app.Listen(":3000")
	if err != nil {
		log.Fatalf("Oops: %v", err)
	}
}
