// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 07
// Apply a discount to a shopping cart.

let cartTotal = 1500;
let isPremiumMember = true;
let finalAmount = cartTotal;

if (cartTotal >= 1000) {
    if (isPremiumMember) {
        finalAmount = cartTotal * 0.80;
    } else {
        finalAmount = cartTotal * 0.90;
    }
}

console.log("Final Amount: ₹" + finalAmount);

// Output:
// Final Amount: ₹1200