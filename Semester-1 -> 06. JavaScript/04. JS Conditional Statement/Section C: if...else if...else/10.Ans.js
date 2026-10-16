// Assignment: Conditional Statements
// Section: C - if...else if...else Statement
// Question: 10
// Classify a number by its sign and parity.

let number = -7;

if (number === 0) {
    console.log("Zero");
} else if (number > 0 && number % 2 === 0) {
    console.log("Positive Even");
} else if (number > 0 && number % 2 !== 0) {
    console.log("Positive Odd");
} else if (number < 0 && number % 2 === 0) {
    console.log("Negative Even");
} else {
    console.log("Negative Odd");
}

// Output:
// Negative Odd