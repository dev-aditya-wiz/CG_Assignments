let rows6 = 5;
for (let i = 1; i <= rows6; i++) {
  let rowStr = "";
  for (let j = 0; j < i; j++) {
    rowStr += String.fromCharCode(65 + j) + " ";
  }
  console.log(rowStr.trim());
}
