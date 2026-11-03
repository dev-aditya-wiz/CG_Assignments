// Q5. Can an inner function access variables of the outer function? What about the reverse (outer accessing inner variables)? Explain.

// Yes, an inner function can access variables of its outer function because of lexical scope. However, the outer function cannot directly access variables declared inside the inner function.

// Example:
function outer() {
    let a = 10;

    function inner() {
        let b = 20;
        console.log(a); // Accessible --> 10
        console.log(b); // Accessible --> 20
    }

    inner();

    console.log(a); // Accessible  --> 10
    // console.log(b); --> // ReferenceError
}
outer();
