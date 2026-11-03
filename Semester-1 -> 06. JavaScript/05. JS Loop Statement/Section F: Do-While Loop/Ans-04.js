// Q4. Product of Digits
let num_do4 = 234;
let prod_do4 = 1;
do {
  prod_do4 *= num_do4 % 10;
  num_do4 = Math.floor(num_do4 / 10);
} while (num_do4 > 0);
console.log(prod_do4);
