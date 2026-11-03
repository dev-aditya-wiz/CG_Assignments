// Q7. Print Multiples with Conditions
let num_do7 = 1;
do {
  if (num_do7 % 4 === 0 && num_do7 % 8 !== 0) console.log(num_do7);
  num_do7++;
} while (num_do7 <= 100);
