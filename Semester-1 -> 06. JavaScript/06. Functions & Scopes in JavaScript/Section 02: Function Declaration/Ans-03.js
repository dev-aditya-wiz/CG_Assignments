// Q3. What happens when we call a function before its definition?

// The function executes successfully because JavaScript supports hoisting for function declarations.
// This means function declarations can be called before their definition.

// Example:
greet();

function greet() {
    console.log("Hello Student!");
}
