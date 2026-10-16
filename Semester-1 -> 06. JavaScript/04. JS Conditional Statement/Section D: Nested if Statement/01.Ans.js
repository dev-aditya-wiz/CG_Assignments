// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 01
// If a number is greater than 10, check divisibility by 3.

let number = 18;

if (number > 10) {
    if (number % 3 === 0) {
        console.log("Greater than 10 and divisible by 3");
    } else {
        console.log("Greater than 10 but not divisible by 3");
    }
} else {
    console.log("Number is not greater than 10");
}

// Output:
// Greater than 10 and divisible by 3