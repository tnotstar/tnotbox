// 01_variables-and-constants.dart

main() {
	// this is a variable
	var dog1 = "Max";

	// this is a mutable single-assignment variable
	final maleDogs = ["Milo"];
    maleDogs.add("Cooper");                 // Ok
    //maleDogs = ["Cooper"];                // Ko

    // alternative `const` syntax (with assignment)
    const femaleDogs = ["Luna", "Bella"];   // Ok
    //femaleDogs.add("Winona");               // Ko
    //femaleDogs = ["Winona"];                // ko

    // non-`const` contructor called
    //const when = [DateTime.now()];          // Ko

    // alternative `const` syntax (without assignment)
    foo(const [7, 8, 9]);                   // Ok
    //foo(const [DateTime.now()]);          // Ko
}

foo(something) {
    // ...
}

// EOF
