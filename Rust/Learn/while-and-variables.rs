/*
 * while-and-variables.rs - an example with a "while" statement and some
 * variable declarations.
 */

fn main() {
    let top = 10;
    let mut counter = 0;

    while counter < top {
        println("Hello, world!");
        counter += 1;
    }
}

