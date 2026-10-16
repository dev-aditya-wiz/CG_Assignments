// Assignment: Conditional Statements
// Section: C - if...else if...else Statement
// Question: 09
// Find the highest of three subject marks.

let marks1 = 76;
let marks2 = 91;
let marks3 = 84;

if (marks1 >= marks2 && marks1 >= marks3) {
    console.log("Highest mark: " + marks1);
} else if (marks2 >= marks1 && marks2 >= marks3) {
    console.log("Highest mark: " + marks2);
} else {
    console.log("Highest mark: " + marks3);
}

// Output:
// Highest mark: 91