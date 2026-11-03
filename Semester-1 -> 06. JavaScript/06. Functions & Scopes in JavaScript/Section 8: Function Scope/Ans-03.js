// Q3.Write a function demoScope that contains a local variable value = 50.
//  Print the variable inside the function. Then try accessing the same variable outside and explain the output / error.
function demoScope() {
    let value = 50;
    console.log(value);
}

demoScope();

console.log(value);
