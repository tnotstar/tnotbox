/* hello.go */

package main

import "github.com/astaxie/beego"

type MainController struct {
    beego.Controller
}

func (this *MainController) Get() {
    this.Ctx.WriteString("Hello, world!\n")
}

func main() {
    beego.Router("/", &MainController{})
    beego.Run()
}

/* EOF */