// Q5. Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.

// Yes, a function can be called without arguments. Its parameters get the value undefined by default.

// Example:
function greet(name) {
    console.log(name);
}

greet();
