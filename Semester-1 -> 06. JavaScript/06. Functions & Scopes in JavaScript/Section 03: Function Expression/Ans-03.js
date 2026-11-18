// Q3. What happens when we call a function expression before its definition?

// It gives a ReferenceError when the function expression is assigned to a let or const variable and called before initialization.
// This happens because let and const cannot be accessed before initialization.

// Example:
showMessage();

const showMessage = function() {
    console.log("Hello!");
};
