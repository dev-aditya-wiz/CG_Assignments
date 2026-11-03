// Q6. Sum of Digits
let num6 = 4729;
let digitSum = 0;
while (num6 > 0) {
  digitSum += num6 % 10;
  num6 = Math.floor(num6 / 10);
}
console.log(digitSum);
