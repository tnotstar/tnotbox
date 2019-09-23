// Stolen from: https://doc.rust-lang.org/rust-by-example/primitives.html

#[allow(unused_variables,unused_assignments)]
fn main() {
    // Variables can be type annotated
    let logical: bool = true;

    let a_float: f64 = 1.0;          // Regular annotation
    let a_int = 5i32;                // Suffix annotation

    // Or a default will be used
    let default_float = 3.0;         // Inferred type is: f64
    let default_integer = 7;         // Inferred type is: i32

    // A type can also be inferred from context
    let mut inferred_type = 12;      // Type i64 is inferred from another line
    inferred_type = 4294967296i64;

    // A mutable variable's value can be changed
    let mut mutable = 12;            // Mutable i32
    mutable = 21;

    // Following line has an error! The type of a variable can't be changed
    //mutable = true;

    // Variables can be overwritten with "shadowing"
    let mutable = true;
}