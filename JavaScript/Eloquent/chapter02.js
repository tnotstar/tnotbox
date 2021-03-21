#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

//
// chapter02.js – some code from chapter 2
//

// the simplest kind of statement
1;
!false;

// to hold values, we use variables
var caught = 5 * 5;
var ten = 10;
console.log(ten);

// assignment operator `=` can overwrite variables' values
var mood = "light";
console.log(mood);

mood = "dark";
console.log(mood);

// some operators may assign and retrieve at same statement
var luigisDebt = 100;
console.log(luigisDebt);
luigisDebt -= 35;
console.log(luigisDebt);

// simple `var` statements may define multiple variables
var one = 1, two = 2;
console.log(one + two);

// these are current reserved words
console.log(
    "break case catch continue debugger default delete\n" +
    "do else false finally for function if implements\n" +
    "in instanceof interface let new null package private\n" +
    "protected public return static switch throw true\n" +
    "try typeof var void while with yield this"
);

// `console.log` is a function...
console.log(console.log);

// ...useful for print current variable values!
var x = 30;
console.log("the value of `x` is", x);

// the `Math.max` function takes any number of values
console.log(Math.max(1, 2, 3, 4, 5));

// browsers also have some interactive functions
//alert("Good morning!");
//confirm("Shall we, then?");
//prompt("Tell me everything you know", "...");

// statements are executed from top to bottom
var theNumber = Math.random();
console.log("Your number is the square root of", theNumber * theNumber);

// conditional statements are as in `C`
var theNumber = Math.random();
if (!isNaN(theNumber))
    console.log("Your number is the square root of", theNumber * theNumber);
else
    console.log("Hey. Why didn't you give me a number?");





// EOF
