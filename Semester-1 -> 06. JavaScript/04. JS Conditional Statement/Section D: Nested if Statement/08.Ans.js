// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 08
// Check if a number is positive, even, and divisible by 4.

let number = 12;

if (number > 0) {
    if (number % 2 === 0) {
        if (number % 4 === 0) {
            console.log("Positive Even and Divisible by 4");
        } else {
            console.log("Positive Even but not divisible by 4");
        }
    } else {
        console.log("Positive Odd Number");
    }
} else {
    console.log("Not a Positive Number");
}

// Output:
// Positive Even and Divisible by 4