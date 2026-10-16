// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 03
// Check whether a student passed and earned distinction.

let marks = 86;

if (marks >= 40) {
    console.log("Passed");

    if (marks >= 80) {
        console.log("Passed with Distinction");
    }
} else {
    console.log("Failed");
}

// Output:
// Passed
// Passed with Distinction