/* This is a multi-line comment:
   This code reverses a string
 */
let value = "Reverse Me"
let reversedValue = ""

value.split("").forEach((ch) => {
    reversedValue = ch + reversedValue
})

console.log(reversedValue)

// versus

function reverseString(input) {
    let output = ""
    input.split("").forEach((ch) => {
        output = ch + output
    })
    return output
}

console.log("This `reverseString(...) = '%s'` function doesn't need any comment",
    reverseString("Reverse Me"))
