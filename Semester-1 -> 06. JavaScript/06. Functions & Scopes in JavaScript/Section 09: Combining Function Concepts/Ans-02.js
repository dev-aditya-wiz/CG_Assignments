// Q2. Create a function billCalculator(item1, item2, item3) that returns the total amount and also mentions if the customer gets a discount (total ≥ 1000 → "Discount Applied", otherwise "No Discount").
function billCalculator(item1, item2, item3) {
    let total = item1 + item2 + item3;
    let message;

    if (total >= 1000) {
        message = "Discount Applied";
    } else {
        message = "No Discount";
    }

    return "Total: " + total + " - " + message;
}

console.log(billCalculator(400, 350, 500));
console.log(billCalculator(200, 300, 100));
