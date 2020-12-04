#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

// hello.js - a simple `Hello, World!` web server from node's home page

var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello, World!\n');
}).listen(8081, 'localhost');
console.log('Server running at http://localhost:8081/');

// EOF
