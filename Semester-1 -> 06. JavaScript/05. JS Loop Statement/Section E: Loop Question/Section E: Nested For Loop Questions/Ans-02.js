let rows2 = 4;
for (let i = 1; i <= rows2; i++) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    rowStr += i + " ";
  }
  console.log(rowStr.trim());
}
