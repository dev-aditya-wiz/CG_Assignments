// Assignment: Conditional Statements
// Section: D - Nested if Statement
// Question: 06
// Check email for @, .com, and length greater than 10.

let email = "student@example.com";

if (email.includes("@")) {
    if (email.endsWith(".com")) {
        if (email.length > 10) {
            console.log("Valid Email");
        } else {
            console.log("Email is too short");
        }
    } else {
        console.log("Email must end with .com");
    }
} else {
    console.log("Email must contain @");
}

// Output:
// Valid Email