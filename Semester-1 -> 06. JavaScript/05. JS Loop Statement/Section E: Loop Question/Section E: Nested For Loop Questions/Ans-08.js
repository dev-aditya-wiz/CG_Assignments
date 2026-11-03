let rows8 = 5;
for (let i = rows8; i >= 1; i--) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    rowStr += "*";
  }
  console.log(rowStr);
}
