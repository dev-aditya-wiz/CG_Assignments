// Q4. Count the Digits
let num4 = 58372;
let count = 0;
while (num4 > 0) {
  count++;
  num4 = Math.floor(num4 / 10); // Removes the last digit
}
console.log(count);
