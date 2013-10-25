#!/usr/bin/env node

if (process.argv.length < 3) {
    console.error("invalid command line arguments");
    console.debug("Number of arguments:", process.argv.length);
    console.debug("Argument values:", process.argv);
    console.log("usage: node cmdline.js <message>");
    process.exit(1);
}

var args = process.argv.slice(2);
var message = args.shift();

console.log('This is the message: "' + message + '"\n\n');

// EOF