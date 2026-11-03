// Q9. Find the Greatest Common Divisor (GCD)
let a_do9 = 48;
let b_do9 = 18;
do {
  let rem_do9 = a_do9 % b_do9;
  a_do9 = b_do9;
  b_do9 = rem_do9;
} while (b_do9 !== 0);
console.log(a_do9);
