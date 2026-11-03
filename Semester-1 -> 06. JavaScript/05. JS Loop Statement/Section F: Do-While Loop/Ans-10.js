// Q10. Convert Decimal to Binary
let num_do10 = 13;
let bin_do10 = "";
let temp_do10 = num_do10;
do {
  bin_do10 = (temp_do10 % 2) + bin_do10;
  temp_do10 = Math.floor(temp_do10 / 2);
} while (temp_do10 > 0);
console.log(bin_do10);
