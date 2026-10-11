// A product costs ₹499. A customer has ₹500. Write conditions using >= and < to decide if the customer can buy it and if any change will be left.

let productPrice = 499;
let customerMoney = 500;
let canBuy = customerMoney >= productPrice;
let change = customerMoney - productPrice;
let insufficientMoney = customerMoney < productPrice;
let hasChange = customerMoney > productPrice;

console.log("Product Price: ₹" + productPrice);
console.log("Customer's Money: ₹" + customerMoney);
console.log("Can Buy Product:", canBuy);
console.log("Insufficient Money:", insufficientMoney);
console.log("Will Receive Change:", hasChange);
console.log("Change Amount: ₹" + change);