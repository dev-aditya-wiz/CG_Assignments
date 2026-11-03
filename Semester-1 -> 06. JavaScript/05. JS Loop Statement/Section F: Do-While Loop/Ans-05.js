// Q5. Find the First Digit
let num_do5 = 58372;
if (num_do5 >= 10) {
  do {
    num_do5 = Math.floor(num_do5 / 10);
  } while (num_do5 >= 10);
}
console.log(num_do5);
