// Q2. Create a function calculateFinal(m1, m2) that has an inner function getTotal to add the marks.
//  Use the inner function and return a message: "Final marks = " followed by the total.
function calculateFinal(m1, m2) {

    function getTotal() {
        return m1 + m2;
    }

    return "Final marks = " + getTotal();
}

console.log(calculateFinal(80, 90));
