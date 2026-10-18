let num = -7;
let result = num === 0 ? "Zero" : num > 0 ? (num % 2 === 0 ? "Positive Even" : "Positive Odd") : (num % 2 === 0 ? "Negative Even" : "Negative Odd");
console.log(result);

// Negative Odd