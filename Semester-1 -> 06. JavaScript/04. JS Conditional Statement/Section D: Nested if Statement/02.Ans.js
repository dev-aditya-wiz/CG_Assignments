// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 02
// Check age and voter ID.

let age = 22;
let hasVoterID = true;

if (age >= 18) {
    if (hasVoterID) {
        console.log("Can Vote");
    } else {
        console.log("Voter ID Required");
    }
} else {
    console.log("Not Eligible by Age");
}

// Output:
// Can Vote