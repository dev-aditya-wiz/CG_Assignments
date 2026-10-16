// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 10
// Check eligibility for the final exam.

let isPresent = true;
let internalMarks = 34;
let externalMarks = 72;

if (isPresent) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        } else {
            console.log("External marks are insufficient");
        }
    } else {
        console.log("Internal marks are insufficient");
    }
} else {
    console.log("Student is absent");
}

// Output:
// Eligible for Final Exam