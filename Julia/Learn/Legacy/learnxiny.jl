#
# learnxiny.jl - this is my own version of `http://learnxinyminutes.com/docs/julia/`
#

# Overview #

#= ==========================================================
  Julia is a new homoiconic functional language focused on
  technical computing. While having the full power of
  homoiconic macros, first-class functions, and low-level
  control, Julia is as easy to learn and use as Python.
========================================================== =#

# Comments #

# single line comments start with a hash (pound) symbol.

#= Mutiple line
   comments need '#=' as BOT and '=#' as EOT.
    #=
     They can be nested!
    =#
=#


# Primitive datatypes and its operators #

## Everything in Julia is an expression. ##

### Expressions have a type ###

#### Integers

3           # => 3 and is a literal of type `Int64`.

#### Floating point numbers

3.2         # => 3.2 and is a literal of type `Float64`.

#### Complex numbers

2 + im      # => 2 + 1i and is a literal of type `Complex{Int64}`.
2.4 + im    # => same as above but with type `Complex{Float64}`.
0.3im       # => Íbidem.

#### Rationals

2//3        # => 2/3 and is a literal of type `Rational{Int64}`.


### Expressions need operators ###

1 + 1       # => 2 plus operator of given types (e.g. `Int64` x `Int64` => `Int64`).
1 + 1.0     # => 2.0 plus operator coerced to `Float64`.
8 - 2       # => 6 minus operator (as above).
10 * 2      # => 20 multiplication operator (as above).
35 / 5      # => 7.0 divide operator (this will always be `Float64`).
div(35, 5)  # => 7 integer division operator (as obvious will be `Int64`).
35 % 5      # => 0 remainder or modulos operator.
5 \ 35      # => 7.0 same as `35 / 5` (so what?).
2 ^ 3       # => 8 power operator.
2 ^ 0.5     # => 1.4142135623730951 a power used to calculate the square root.
2 ^ (1//2)  # => 1.4142135623730951 same as above, but note parenthesis :-S

#### Parenthesis are useful!

1 + 3 * 2   # => 7 parenthesis are optional,
1 + (3 * 2) # => 7 if we understand operator preference,
(1 + 3) * 2 # => 8 otherwise put them all.



# EOF
