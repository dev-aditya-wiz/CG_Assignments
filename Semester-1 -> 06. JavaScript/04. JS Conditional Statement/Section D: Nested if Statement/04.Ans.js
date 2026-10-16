// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 04
// Simple ATM system: verify PIN and withdrawal balance.

let enteredPIN = 1234;
let correctPIN = 1234;
let balance = 5000;
let withdrawal = 1500;

if (enteredPIN === correctPIN) {
    if (balance >= withdrawal) {
        balance = balance - withdrawal;

        console.log("Withdrawal Successful");
        console.log("Remaining Balance: ₹" + balance);
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}

// Output:
// Withdrawal Successful
// Remaining Balance: ₹3500