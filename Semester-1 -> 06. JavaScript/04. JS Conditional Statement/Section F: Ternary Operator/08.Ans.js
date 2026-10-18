let year = 2024;
let result = year % 4 === 0 ? (year % 100 !== 0 ? "Leap Year" : (year % 400 === 0 ? "Leap Year" : "Not a Leap Year")) : "Not a Leap Year";
console.log(result);

// leap year