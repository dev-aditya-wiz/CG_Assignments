// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 09
// Check job eligibility by age, degree, and experience.

let age = 25;
let hasGraduationDegree = true;
let experienceYears = 3;

if (age >= 21 && age <= 30) {
    if (hasGraduationDegree) {
        if (experienceYears >= 2) {
            console.log("Eligible for Interview");
        } else {
            console.log("Not enough experience");
        }
    } else {
        console.log("Graduation Degree Required");
    }
} else {
    console.log("Age is not within the required range");
}

// Output:
// Eligible for Interview