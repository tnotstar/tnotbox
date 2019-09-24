// Stolen from: https://itnext.io/e17c35a60c54

main() {
    // variables without a data type must be defined with data type identifiers
    // variables without an initial value have `null` values
    int myNumber;
    double myDouble;
    String myString;

    // we can also assign `null` to a variable at variable declaration
    // or at anytime
    // `null` signifies no-value or empty-value
    bool myBoolean = null;

    print(myNumber);     // Print `null`
    print(myDouble);     // Print `null`
    print(myString);     // Print `null`
    print(myBoolean);    // Print `null`
}
