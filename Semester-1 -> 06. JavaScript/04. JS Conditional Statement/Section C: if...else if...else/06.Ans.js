// Assignment: Conditional Statements
// Section: C - if...else if...else Statement
// Question: 06
// Check whether a day is a weekday or weekend.

let day = 6;

if (day >= 1 && day <= 5) {
    console.log("Weekday");
} else if (day === 6 || day === 7) {
    console.log("Weekend");
} else {
    console.log("Invalid Day");
}

// Output:
// Weekend