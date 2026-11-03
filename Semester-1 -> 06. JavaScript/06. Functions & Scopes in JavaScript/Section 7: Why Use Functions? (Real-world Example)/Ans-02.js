// Q2.Create a function calculateSimpleInterest(principal, rate, time) that returns the simple interest.
//  Use the function to find interest for two different sets of values.

// Formula: Simple Interest = (Principal × Rate × Time) / 100
function calculateSimpleInterest(principal, rate, time) {
    return (principal * rate * time) / 100;
}

console.log(calculateSimpleInterest(10000, 5, 2));
console.log(calculateSimpleInterest(20000, 6, 3));
