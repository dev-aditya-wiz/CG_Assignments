// Assignment: Conditional Statements
// Section: C - if...else if...else Statement
// Question: 02
// Calculate tax based on income brackets.

let income = 500000;
let tax;

if (income < 300000) {
    tax = 0;
} else if (income <= 700000) {
    tax = income * 0.05;
} else if (income <= 1000000) {
    tax = income * 0.10;
} else {
    tax = income * 0.15;
}

console.log("Tax amount: ₹" + tax);

// Output:
// Tax amount: ₹25000

// Note: The rate for the matching bracket is applied
// to the entire income.