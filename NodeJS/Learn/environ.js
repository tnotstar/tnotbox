#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

// environ.js - an example of getting environment variables

console.log("Testing environment objects...");

console.dir(process.env);

console.log(process.env['http_proxy']);
console.log(process.env.http_proxy);

// EOF
