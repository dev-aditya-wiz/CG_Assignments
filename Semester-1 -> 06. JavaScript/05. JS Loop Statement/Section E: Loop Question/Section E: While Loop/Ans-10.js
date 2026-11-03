// Q10. Convert Decimal to Binary
let num10 = 13;
let binaryStr = "";
while (num10 > 0) {
  let remainder = num10 % 2;
  binaryStr = remainder + binaryStr;
  num10 = Math.floor(num10 / 2);
}
console.log(binaryStr || "0");
