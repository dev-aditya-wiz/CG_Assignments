let rows10 = 5;
for (let i = rows10; i >= 1; i--) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    rowStr += j + " ";
  }
  console.log(rowStr.trim());
}
