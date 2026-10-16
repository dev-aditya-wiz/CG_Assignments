// Assignment: Conditional Statements
// Section: C - if...else if...else Statement
// Question: 07
// Calculate an electricity bill based on units.

let units = 120;
let bill;

if (units < 0) {
    console.log("Invalid units");
} else if (units <= 50) {
    bill = units * 2;
    console.log("Electricity Bill: ₹" + bill);
} else if (units <= 150) {
    bill = units * 4;
    console.log("Electricity Bill: ₹" + bill);
} else {
    bill = units * 6;
    console.log("Electricity Bill: ₹" + bill);
}

// Output:
// Electricity Bill: ₹480

// Note: The rate for the matching range is applied
// to all units.