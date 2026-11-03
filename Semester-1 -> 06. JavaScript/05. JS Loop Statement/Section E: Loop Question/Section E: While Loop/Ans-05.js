// Q5. Reverse a Number
let num5 = 12345;
let reversed = 0;
while (num5 > 0) {
  let lastDigit = num5 % 10;
  reversed = (reversed * 10) + lastDigit;
  num5 = Math.floor(num5 / 10);
}
console.log(reversed);
