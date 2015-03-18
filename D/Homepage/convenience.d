#!/usr/bin/env rdmd

// D allows writing large code fragments without redundantly specifying types,
// like dynamic languages do. On the other hand, static inference deduces
// types and other code properties, giving the best of both the static and the
// dynamic worlds.

import std.stdio;

void main() {

    // Define an array of numbers, double[]. Compiler recognizes the common
    // type of all initializers.
    auto arr = [1, 2, 3.14, 5.1, 6];

    // Dictionary that maps string to int, type is spelled int[string]
    auto dictionary = ["one": 1, "two": 2, "three": 3];

    // Calls the min function defined below
    auto x = min(arr[0], dictionary["two"]);

    writeln("x = ", x);
}

auto min(T1, T2)(T1 lhs, T2 rhs) {
    return rhs < lhs ? rhs : lhs;
}

