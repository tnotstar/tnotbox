#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

if (process.argv.length < 3) {
    console.error("Number of arguments:", process.argv.length);
    console.error("Argument values:", process.argv);
    console.error("usage: ", process.argv[0], process.argv[1], "<message>");
    process.exit(1);
}

var args = process.argv.slice(2);
var message = args.shift();

console.log('This is the message: "' + message + '"\n\n');

// EOF
