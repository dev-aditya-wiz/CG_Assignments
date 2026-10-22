// Write a for loop that prints the first 20 Fibonacci numbers (starting with 0 and 1).

// Fibonacci numbers --> starts from = 0 & 1
// continues sum of the series --> 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

let a = 0;
let b = 1;
let fibonacciSeries = "0 1 ";
for (let i=1; i<=18; i++) {
    let c = a + b;
    fibonacciSeries += c + " ";
    a = b;
    b = c;
}
console.log(fibonacciSeries)

// 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 