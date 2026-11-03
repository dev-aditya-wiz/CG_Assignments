// Q5. What will happen if a global variable and a local variable have the same name? Which one will the function use? Explain briefly.

// The function will use the local variable because local variables have priority over global variables inside their scope.

// Example:
let x = 10;

function showValue() {
    let x = 50;
    console.log(x);
}

showValue();
console.log(x);
