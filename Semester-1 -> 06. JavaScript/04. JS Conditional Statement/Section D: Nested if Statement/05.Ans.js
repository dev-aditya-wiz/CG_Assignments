// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 05
// Check whether a year is a leap year using nested if.

let year = 2000;

if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}

// Output:
// Leap Year