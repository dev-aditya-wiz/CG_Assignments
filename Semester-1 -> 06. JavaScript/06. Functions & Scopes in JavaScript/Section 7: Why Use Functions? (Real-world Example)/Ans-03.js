// Q3. Without using a function, write code to find the average of three numbers twice (for two students).
//  Then rewrite the same logic using a single function findAverage(a, b, c) and call it twice.

// Without function:
let avg1 = (80 + 70 + 90) / 3;
console.log("Student 1 Average:", avg1);

let avg2 = (60 + 75 + 85) / 3;
console.log("Student 2 Average:", avg2);


// With function:
function findAverage(a, b, c) {
    return (a + b + c) / 3;
}

console.log("Student 1 Average:", findAverage(80, 70, 90));
console.log("Student 2 Average:", findAverage(60, 75, 85));
