// Lesson 1: Introduction
console.log('Welcome to JavaScript!')

// Lesson 2: Variables
let weather = "cloudy"
console.log(weather)

weather = "sunny"
console.log(weather)

const name = 'Antonio'
console.log(name)

// Lesson 3: Concatination
let day = 'Saturday'
let phrase = 'Today is ' + day + ' and the weather is ' + weather
console.log(phrase)

let phrase2 = `Today is ${day} and the weather is ${weather}`
console.log(phrase2)

// Lesson 4: Numbers
let result = 2 + 5
console.log(result)

let width = 5
let length = 8
result = width * length
console.log(result)

// Lesson 5: Math Libraries
let randNumber = Math.random()
console.log(randNumber)

randNumber = 5*Math.random()
console.log(randNumber)

let roundDown = Math.floor(randNumber)
let roundUp = Math.ceil(randNumber)
console.log(roundDown, roundUp)

// Lesson 6: Conditional Statements
let wallet = 20
let trainersPrice = 50
console.log(wallet > trainersPrice)
if (wallet > trainersPrice) {
    console.log('I can go and buy some trainers!')
} else {
    console.log("I don't have enough money to buy the trainers...")
}

let anotherDay = 'Saturday'
if (anotherDay === 'Sunday') {
    console.log('Its weekend lets buy some trainers')
} else {
    console.log("Its still week time, we don't have time for shopping")
}
