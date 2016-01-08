#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

//
// chapter01.js – some code from chapter 1
//

// welcome javascript!
console.log("console.log can write on the screen!");

// these are number values
console.log(13);
console.log(9.81);
console.log(2.99e8);

// these are arithmetic operators
console.log(100 + 4 * 11);
console.log((100 + 4)* 11);

// these are special numbers
console.log(NaN);
console.log(Infinity);
console.log(-Infinity);

// these are string values
console.log("Patch my boat with chewing gum");
console.log('Monkeys wave goodbye');
console.log("This is the first line\nAnd this is the second");
console.log("A newline character is written like \"\\n\".");
console.log("con" + "cat" + "e" + "nate");

// these are unary operators
console.log(typeof 4.5);
console.log(typeof "x");
console.log(-(10 - 2));

// these are boolean values
console.log(3 > 2);
console.log(3 < 2);
console.log("Aardvark" < "Zoroaster");
console.log("Itchy" != "Scratchy");
console.log(NaN == NaN);

// these are logical operators
console.log(true && false);
console.log(true && true);
console.log(false || true);
console.log(false || false);
console.log(1 + 1 == 2 && 10 * 10 > 50);
console.log(true ? 1 : 2);
console.log(false ? 1 : 2);

// these are undefined values
console.log(undefined);

// automatic type conversion works thus
console.log(8 * null);
console.log("5" - 1);
console.log("5" + 1);
console.log("five" + 2);
console.log(false == 0);
console.log(null == undefined);
console.log(null == 0);

// short-circuiting works thus
console.log(null || "user");
console.log("Karl" || "user");

// EOF
