#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

/**
 * Based upon http://unix.stackexchange.com/a/65295 by dancek
 */

console.log("Hello, world!");

// EOF
