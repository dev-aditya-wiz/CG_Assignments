// Explain why "10" > "2" is false but 10 > 2 is true.

let firstValue = "10";
let secondValue = "2";
console.log(firstValue > secondValue);      // false
// Since "1" comes before "2", the string "10" is considered smaller than the string "2".
// When JavaScript compares two strings, it uses lexicographical order rather than comparing their numerical values.

let firstNumber = 10;
let secondNumber = 2;
console.log(firstNumber > secondNumber);     // true
// JavaScript compares their numerical values that's why 10 is greater than 2.
