// Q1.You need to calculate the total marks of three subjects for 4 different students.
//  Write a function getTotal(m1, m2, m3) and call it four times with different marks instead of repeating the addition code.
function getTotal(m1, m2, m3) {
    return m1 + m2 + m3;
}

console.log("Student 1:", getTotal(80, 75, 90));
console.log("Student 2:", getTotal(65, 70, 85));
console.log("Student 3:", getTotal(90, 95, 88));
console.log("Student 4:", getTotal(55, 60, 70));
