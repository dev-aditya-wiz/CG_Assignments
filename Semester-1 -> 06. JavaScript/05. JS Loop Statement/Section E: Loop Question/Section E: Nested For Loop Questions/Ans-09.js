let rows9 = 5;
for (let i = rows9; i >= 1; i--) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    rowStr += i + " ";
  }
  console.log(rowStr.trim());
}
