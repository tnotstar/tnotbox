// Stolen from: https://doc.rust-lang.org/rust-by-example/hello.html

// This is a comment, and is ignored by the compiler

// This is the main function
fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    println!("Hello, world!");
    // println! is a macro that prints text to the console.
}

// A binary can be generated using the Rust compiler: rustc hello.rs
// rustc will produce a hello binary that can be executed: ./hello