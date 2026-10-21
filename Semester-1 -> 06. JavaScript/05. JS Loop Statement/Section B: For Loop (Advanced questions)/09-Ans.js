let marks = [45, 78, 90, 32, 56, 88];
let sum = 0;
for (let i = 0; i < marks.length; i++) {
    sum = sum + marks[i];
}

let avg = sum / marks.length;
let count = 0;
for (let i = 0; i < marks.length; i++) {
    if (marks[i] > avg) {
        count++;
    }
}

console.log("Average =", avg);
console.log("Above average =", count);

// Average = 64.83333333333333
// Above average = 3