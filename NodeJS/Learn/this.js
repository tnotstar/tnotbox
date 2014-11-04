#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

var ctor = function (options) {

    if (!options)
        throw new Error("Missing 'options' value");

    var self = this;
    self.options = options;

    console.log("> ctor(options): self = ", self, "!");
}

ctor({name: "John Doe"});

var object = new ctor({name: "John Doe"});

// EOF
