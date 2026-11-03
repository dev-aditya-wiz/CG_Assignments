// Q6. Calculate a Power
let base_do6 = 3;
let exp_do6 = 4;
let res_do6 = 1;
let c_do6 = 1;
if (exp_do6 > 0) {
  do {
    res_do6 *= base_do6;
    c_do6++;
  } while (c_do6 <= exp_do6);
}
console.log(res_do6);
